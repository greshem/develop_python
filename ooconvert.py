#!/bin/bash

# ooConvert:  convert openoffice documents to other formats
# Copyright (C) 2007, Metaladder, Inc.
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

##############################################################################
##############################################################################
# This script should be run with the same python interpreter that openoffice
# uses, which is usually included with openoffice:
#
# /path/to/openoffice-2.0.1/program/python.sh
# 
# However, under debian, ubuntu, etc, openoffice uses the system-installed
# python interpreter.  To find which interpreter is being used, look in
# 
# /path/to/openoffice/program/pythonloader.unorc
# 
# If openoffice is using an external python interpreter, modify the following
# LD_LIBRARY_PATH to reflect your openoffice environment and to import uno
# without errors
##############################################################################
##############################################################################

shopt -s -o nounset

### site configuration
#OO_LOGLEVEL=20
#USE_OO_INTERNAL_PYTHON=0 #set to 1 if python is embedded in openoffice
#OOPROGRAM=/usr/lib/openoffice/program #directory containing soffice
#OOPYTHON=${OOPROGRAM}/python.sh"
#OO_EXTERNAL_PYTHON=/usr/bin/python2.3
#OOXVFB="Xvfb"
#OOXWININFO=xwininfo
#OOXVFB_START=0} #first port to try Xvfb on
#OOXVFB_RETRIES:="1000"} #how many successive port to try
#alternatively, put site details in one of these files
[ -r /etc/ooconvert ] && source /etc/ooconvert
[ -r ~/etc/ooconvert ] && source ~/etc/ooconvert
### site configuration end

### configuration defaults start 
# Choose openoffice internal python (1) or external python (0)
: ${OO_LOGLEVEL:=20}
: ${USE_OO_INTERNAL_PYTHON:=0}
: ${OOPROGRAM:="/usr/lib/openoffice/program"}
: ${OOPYTHON:="${OOPROGRAM}/python.sh"}
: ${OO_EXTERNAL_PYTHON:="/usr/bin/python2.3"}
: ${OOXVFB:="Xvfb"}
: ${OOXWININFO:="xwininfo"}
: ${OOXVFB_START:=0}
: ${OOXVFB_RETRIES:="1000"}
### configuration defaults end

LOG_NOTSET=0
LOG_DEBUG=10
LOG_INFO=20
LOG_WARNING=30
LOG_ERROR=40
LOG_CRITICAL=50

OOXVFBJOB=

oo_log () {
	if [ "$OO_LOGLEVEL" -le "$1" ]; then
		shift
		printf '%s\n' "$@" >&2
	fi
}

oo_err () {
	exit_status="$1"
	shift
	oo_log $LOG_ERROR "$@"
	exit "$exit_status" 
}

### If an X Server is not detected, try to use Xvfb
if [ ! "${DISPLAY:-}" ]; then
	oo_log $LOG_INFO "\"DISPLAY\" variable is not set.  Attempting Xvfb."
	for i in "$OOXVFB" /usr/bin/X11/Xvfb /usr/X11R6/bin/Xvfb; do
		oo_log "$LOG_INFO" "Trying to invoke $i"
		$i >& /dev/null
		if [ $? != 127 ]; then #127 is the bash shell code for "not found"
			OOXVFB="$i"
			break
		fi
		OOXVFB=
	done
	unset i
	if [ "$OOXVFB" ]; then 
		oo_log $LOG_INFO "Xvfb is installed."
		for i in "$OOXWININFO" "$(dirname "$OOXVFB")/xwininfo"; do
			$i >& /dev/null
			if [ $? != 127 ]; then #127 is the bash shell code for "not found"
				OOXWININFO="$i"
				break
			fi
			OOXWININFO=
		done
		[ "$OOXWININFO" ] || oo_err 130 "ooxwininfo not found"
		unset i
		((last=$OOXVFB_START+$OOXVFB_RETRIES))
		while :; do
			"$OOXVFB" :$OOXVFB_START -screen scrn 1280x1024x16 &
			OOXVFBJOB=$!
			export DISPLAY=":$OOXVFB_START"
			sleep 1
			ps "$OOXVFBJOB" && "$OOXWININFO" -root && break
			ps "$OOXVFBJOB" && : kill "$OOXVFBJOB" 
			oo_log $LOG_INFO "Failed to start Xvfb on display $OOXVFB_START"
			((OOXVFB_START++))
			[ $OOXVFB_START -ge $last ] && \
				oo_err 129 "Xvfb attempts exceeded $OOXVFB_RETRIES"
		done
		oo_log $LOG_INFO "Xvfb started.  Process id:  $OOXVFBJOB"
		oo_log $LOG_INFO "Setting \"Display\" to $DISPLAY for Xvfb"
	fi
fi

case "$USE_OO_INTERNAL_PYTHON" in
	0)
		OOPYTHON="$OO_EXTERNAL_PYTHON"
		export LD_LIBRARY_PATH="$OOPROGRAM${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"
		;;
esac


"$OOPYTHON" - "$@" <<EOF
# OpenOffice1.1 comes with its own python interpreter.
# This Script needs to be run with the python from OpenOffice.org:
#   /opt/OpenOffice.org/program/python or python.sh

#pythonloader.unorc

__doc__="Document converter which uses OO for actual converting"

import sys, os, time, signal
from optparse import OptionParser

#how long should we wait for openoffice to start
OOCONV_MAX_STARTUP_TIME = os.getenv("OOCONV_MAX_STARTUP_TIME")
if not OOCONV_MAX_STARTUP_TIME: OOCONV_MAX_STARTUP_TIME=60
OOCONV_MAX_STARTUP_TIME=int(OOCONV_MAX_STARTUP_TIME)
#what port should openoffice listen on
OOCONV_PORT = os.getenv("OOCONV_PORT")
if not OOCONV_PORT: OOCONV_PORT=2002
OOCONV_PORT = int(OOCONV_PORT)

class Format:
    """
    Describe output format details.
    """
    
    def __init__(self, name, title, filterName, ext, isDefault=False):
        """
        name       -- short name which is used as argument of '--format' option.
        title      -- human readable format title
        filterName -- filter name which is used in OpenOffice API
        ext        -- format extension (case insensitive)
        isDefault  -- flag which indicates that this format is used as default
                      format for given extension.  for example there are
                      several MS Office formats which share the same extension,
                      but when we try to guess format by extension we need to
                      choose one.  It will be format which has isDefault=True.
        """
        self.name = name
        self.title = title
        self.filterName = filterName
        self.ext = ext.lower()
        self.isDefault = isDefault


FORMATS = (Format('Word97', 'MS Word 97', 'MS Word 97', 'doc', True),
           Format('Word95', 'MS Word 95', 'MS Word 95', 'doc', False),
           Format('Word6.0', 'MS WinWord 6.0', 'MS WinWord 6.0', 'doc', False),
           Format('HTML', 'HTML (StarWriter)', 'HTML (StarWriter)', 'html', True),
           Format('PDF', 'PDF', 'writer_pdf_Export', 'pdf', True),
           Format('RTF', 'Rich Text Format', 'Rich Text Format', 'rtf', True),
           Format('SOXML', 'StarOffice XML (Writer)', 'StarOffice XML (Writer)', 'xml', True))

FORMAT_EXTS = {}
FORMAT_NAMES = {}

## fill format indexes
for f in FORMATS:
    if f.ext not in FORMAT_EXTS or f.isDefault:
        FORMAT_EXTS[f.ext] = f
    FORMAT_NAMES[f.name.lower()] = f
    

def importUNO():
    """
    Import UNO modules
    """
    import uno
    from com.sun.star.beans import PropertyValue
    globals()['uno'] = uno
    globals()['PropertyValue'] = PropertyValue
    

class OOConverter:
    """
    Convert documents by means of Open Office.
    """
    
    def __init__(self, desktop):
        self.desktop = desktop

    def convert(self, fromFile, toFile, format):
        """
        fromFile -- source file name
        toFile   -- destination file name
        format   -- instance of Format class
        """
        desktop = self.desktop
        fromFile=os.path.abspath(fromFile)
        url="file://%s" % fromFile
        properties=[]
        p=PropertyValue()
        p.Name="Hidden"
        p.Value=True
        properties.append(p)
        doc=desktop.loadComponentFromURL(
            url, "_blank", 0, tuple(properties));
        if not doc:
            print "Failed to open '%s'" % file
            return False
        # Save File
        properties=[]
        p=PropertyValue()
        p.Name="Overwrite"
        p.Value=True
        properties.append(p)
        p=PropertyValue()
        p.Name="FilterName"
        p.Value=format.filterName
        properties.append(p)
        p=PropertyValue()
        p.Name="Hidden"
        p.Value=True
        url_save="file://%s" % os.path.abspath(toFile)
        try:
            doc.storeToURL(
                url_save, tuple(properties))
        except:
            print "Failed while writing: '%s'" % file
        doc.dispose()
        return True



class FileIterator:
    """
    Iterate over each conversion task.
    A conversion task consists of source file name,
    destination file name and format
    """
    def __init__(self, sources, dest, format):
        self.sources = sources
        self.dest = dest
        self.isDestDir = False
        if os.path.isdir(dest):
            self.isDestDir = True
        self.format = format
        self.siter = iter(self.sources)

    def __iter__(self):
        return self

    def next(self):
        src = self.siter.next()
        return (src, self._getDestFN(src), self.format)

    def _getDestFN(self, src):
        if not self.isDestDir:
            return self.dest
        base, ext = os.path.splitext(os.path.basename(src))
        return os.path.join(self.dest, base)+'.'+self._getFormatExt()

    def _getFormatExt(self):
        return self.format.ext

    

def expandSources(sources):
    result = []
    for src in sources:
        if os.path.isdir(src):
            result.extend([os.path.join(src,entry) for entry in os.listdir(src) if os.path.isfile(os.path.join(src,entry))])
        elif os.path.isfile(src):
            result.append(src)
    return result


def guessFormat(fileName):
    """
    Guess format by the file name extension
    """
    name, ext = os.path.splitext(fileName)
    ext = ext[1:]
    if not ext: return None    
    return FORMAT_EXTS.get(ext, None)
    

def startOOAndConnect():
    """
    Start OO in child process and connect to them.
    Return OO component context object.
    """
    pid = os.fork()
    if not pid:
      pid = os.getpid()
      os.setpgid(pid,pid)
      os.system("soffice -headless -norestore '-accept=socket,host=localhost,port=%s;urp;' &" % OOCONV_PORT)
      while 1:
          time.sleep(1)
    else:
        limit = time.time() + OOCONV_MAX_STARTUP_TIME
        ctx = None
        context = uno.getComponentContext()
        resolver=context.ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", context)

        while time.time() < limit:
            try:
                ctx = resolver.resolve(
                    "uno:socket,host=localhost,port=%s;urp;StarOffice.ComponentContext" % OOCONV_PORT)
                break
            except:
                pass
            time.sleep(5)
        if ctx is None:
            pgid = os.getpgid(pid)
            os.killpg(pgid, signal.SIGTERM)                        
            return None, None
        return ctx, pid


def connect(host='localhost', port=OOCONV_PORT):
    """
    Try to connect to the running OO instance
    """
    context = uno.getComponentContext()
    resolver=context.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", context)
    try:
        return resolver.resolve(
            "uno:socket,host=%s,port=%s;urp;StarOffice.ComponentContext" % (host, port))
    except:
        pass
    return None

    
def main():
    usage1 = "usage: %prog <source file> <destination file> [options]"
    usage2 = "   or: %prog sources... <destination dir> [options]"
    parser = OptionParser(usage1+'\n'+usage2)
    parser.add_option('-f','--format', dest='format',
                      help='Output file format', metavar='format')
    parser.add_option('-p','--oopath', dest='oopath', metavar='path',
                      help='Path to OO program directory')
    parser.add_option('-l','--list', dest='listFormats', action="store_true",
                      default=False,
                      help='List all available formats')
    parser.add_option('-a' ,'--laddr', dest='listener', metavar='host[:port]',
                      help='If this option exists then try to connect to given OO listener address')
    
    opts, args = parser.parse_args()

    if opts.listFormats:
        print 'Available formats: %s' % ', '.join([f.name for f in FORMATS])
        sys.exit(0)
        
    if len(args)<1:
        parser.error('incorrect number of arguments')

    if len(args) == 1:
        dest = os.getcwd()
        sources = [os.path.abspath(args[0])]
        isDestDir = True
    else:
        dest = os.path.abspath(args[-1])
        sources = [os.path.abspath(src) for src in args[:-1]]
        isDestDir = os.path.isdir(dest)
        ## if we have more than one input files then last argument must be output directory
        if len(args) > 2 and not isDestDir:
            parser.error('last argument must be directory')
        if not isDestDir and len(args)==2:
            src = sources[0]
            if not os.path.isfile(src):
                parser.error('first argument must be a path to the file in this case')

    format = opts.format

    if format:
        format=format.lower()
        if not FORMAT_NAMES.has_key(format):
            parser.error("Unknown format: %s" % format)

    ## if destination is directory then format option is required
    if isDestDir and not format:
        parser.error('format option is required')

    ## try to guess format by the output filename extension
    if not isDestDir and not format:
        format = guessFormat(dest)
        if not format:
            parser.error("can't guess output format")
    elif format:
        format = FORMAT_NAMES[format]

    if opts.oopath:
        os.environ['PATH'] = '%s:%s' % (os.environ['PATH'], opts.oopath)
        sys.path.append(opts.oopath)

    importUNO()

    sources = expandSources(sources)

    pid = None
    
    if opts.listener:
        parts = opts.listener.split(':')
        host = parts[0]
        port=2002
        if len(parts)>1:
            port = int(parts[1])
        ctx = connect(host, port)
    else:
        ctx, pid = startOOAndConnect()
        
    if ctx is None:
        print "Could not connect to running openoffice"
        sys.exit(1)

    try:
        smgr=ctx.ServiceManager
        desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop",ctx)
        oo = OOConverter(desktop)
        iterator = FileIterator(sources, dest, format)
        for fromFile, toFile, format in iterator:
            print 'Converting %s to %s (format: %s)...' % (os.path.basename(fromFile),os.path.basename(toFile), format.title),
            oo.convert(fromFile, toFile, format)
            print 'successfully.'
    finally:
        if pid:
            pgid = os.getpgid(pid)
            os.killpg(pgid, signal.SIGTERM)


if __name__ == '__main__':
    main()

EOF

if [ "$OOXVFBJOB" ]; then
	oo_log $LOG_INFO "Killing Xvfb, running as process number $OOXVFBJOB"
	kill "$OOXVFBJOB"
fi
