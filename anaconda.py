#!/usr/bin/python
#
# anaconda: The Red Hat Linux Installation program
#
# (in alphabetical order...)
#
# Brent Fox <bfox@redhat.com>
# Mike Fulbright <msf@redhat.com>
# Jakub Jelinek <jakub@redhat.com>
# Jeremy Katz <katzj@redhat.com>
# Chris Lumens <clumens@redhat.com>
# Paul Nasrat <pnasrat@redhat.com>
# Erik Troan <ewt@rpath.com>
# Matt Wilson <msw@rpath.com>
#
# ... And many others
#
# Copyright 1999-2007 Red Hat, Inc.
#
# This software may be freely redistributed under the terms of the GNU
# library public license.
#
# You should have received a copy of the GNU Library Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

# This toplevel file is a little messy at the moment...

import sys, os
from optparse import OptionParser

# keep up with process ID of miniwm if we start it

miniwm_pid = None

# Make sure messages sent through python's warnings module get logged.
def AnacondaShowWarning(message, category, filename, lineno, file=sys.stderr):
    log.warning("%s" % warnings.formatwarning(message, category, filename, lineno))

# start miniWM
def startMiniWM(root='/'):
    (rd, wr) = os.pipe()
    childpid = os.fork()
    if not childpid:
	if os.access("./mini-wm", os.X_OK):
	    cmd = "./mini-wm"
	elif os.access(root + "/usr/bin/mini-wm", os.X_OK):
	    cmd = root + "/usr/bin/mini-wm"
	else:
	    return None
	
	os.dup2(wr, 1)
	os.close(wr)
	args = [cmd, '--display', ':1']
	os.execv(args[0], args)
	sys.exit (1)
    else:
	# We need to make sure that mini-wm is the first client to
	# connect to the X server (see bug #108777).  Wait for mini-wm
	# to write back an acknowledge token.
	os.read(rd, 1)

    return childpid

# function to handle X startup special issues for anaconda
def doStartupX11Actions():
    global miniwm_pid

    # now start up mini-wm
    try:
	miniwm_pid = startMiniWM()
	log.info("Started mini-wm")
    except:
	miniwm_pid = None
	log.error("Unable to start mini-wm")

    # test to setup dpi
    # cant do this if miniwm didnt run because otherwise when
    # we open and close an X connection in the xutils calls
    # the X server will exit since this is the first X
    # connection (if miniwm isnt running)
    if miniwm_pid is not None:
	import xutils

	try:
	    if xutils.screenWidth() > 640:
		dpi = "96"
	    else:
		dpi = "75"

	    xutils.setRootResource('Xcursor.size', '24')
	    xutils.setRootResource('Xcursor.theme', 'Bluecurve')
	    xutils.setRootResource('Xcursor.theme_core', 'true')

	    xutils.setRootResource('Xft.antialias', '1')
	    xutils.setRootResource('Xft.dpi', dpi)
	    xutils.setRootResource('Xft.hinting', '1')
	    xutils.setRootResource('Xft.hintstyle', 'hintslight')
	    xutils.setRootResource('Xft.rgba', 'none')
	except:
	    sys.stderr.write("X SERVER STARTED, THEN FAILED");
	    raise RuntimeError, "X server failed to start"

def doShutdownX11Actions():
    global miniwm_pid
    
    if miniwm_pid is not None:
	try:
	    os.kill(miniwm_pid, 15)
	    os.waitpid(miniwm_pid, 0)
	except:
	    pass

# handle updates of just a single file in a python package
def setupPythonUpdates():
    import glob

    # get the python version.  first of /usr/lib/python*, strip off the
    # first 15 chars
    pyvers = glob.glob("/usr/lib/python*")
    pyver = pyvers[0][15:]
    
    try:
	os.mkdir("/tmp/updates")
    except:
	pass

    for pypkg in ("rhpl", "yum", "rpmUtils", "urlgrabber", "pykickstart",
                  "rhpxl", "pirut"):
	if os.access("/mnt/source/RHupdates/%s" %(pypkg,), os.X_OK):
	    try:
		os.mkdir("/tmp/updates/%s" %(pypkg,))
	    except:
		pass

	    # symlink the existing ones
	    for f in os.listdir("/mnt/source/RHupdates/%s" %(pypkg,)):
		os.symlink("/mnt/source/RHupdates/%s/%s" %(pypkg, f),
			   "/tmp/updates/%s/%s" %(pypkg, f))

	# get the libdir.  *sigh*
	if os.access("/usr/lib64/python%s/site-packages/%s" %(pyver, pypkg),
		     os.X_OK):
	    libdir = "lib64"
        elif os.access("/usr/lib/python%s/site-packages/%s" %(pyver, pypkg),
                       os.X_OK):
	    libdir = "lib"
	else:
            # If the directory doesn't exist, there's nothing to link over.
            # This happens if we forgot to include one of the above packages
            # in the image, for instance.
            continue

	if os.access("/tmp/updates/%s" %(pypkg,), os.X_OK):
	    for f in os.listdir("/usr/%s/python%s/site-packages/%s" %(libdir,
								      pyver,
								      pypkg)):
		if os.access("/tmp/updates/%s/%s" %(pypkg, f), os.R_OK):
		    continue
		elif (f.endswith(".pyc") and
		      os.access("/tmp/updates/%s/%s" %(pypkg, f[:-1]),os.R_OK)):
		    # dont copy .pyc files we are replacing with updates
		    continue
		else:
		    os.symlink("/usr/%s/python%s/site-packages/%s/%s" %(libdir,
									pyver,
									pypkg,
									f),
			       "/tmp/updates/%s/%s" %(pypkg, f))

def parseOptions():
    def resolution_cb (option, opt_str, value, parser):
        global runres_override
        parser.values.runres = value
        runres_override = True

    def rootpath_cb (option, opt_str, value, parser):
        if value.startswith("cd:"):
            flags.livecd = True
            value = value[3:]
        parser.values.rootPath = os.path.abspath(value)
        flags.setupFilesystems = False
        flags.rootpath = True

    op = OptionParser()
    # Interface
    op.add_option("-C", "--cmdline", dest="display_mode", action="store_const", const="c")
    op.add_option("-G", "--graphical", dest="display_mode", action="store_const", const="g")
    op.add_option("-T", "--text", dest="display_mode", action="store_const", const="t")

    # Network
    op.add_option("--noipv4", action="store_true", default=False)
    op.add_option("--noipv6", action="store_true", default=False)

    # Method of operation
    op.add_option("--autostep", action="store_true", default=False)
    op.add_option("-d", "--debug", dest="debug", action="store_true", default=False)
    op.add_option("--expert", action="store_true", default=False)
    op.add_option("--kickstart", dest="ksfile")
    op.add_option("-m", "--method", default=None)
    op.add_option("--rescue", dest="rescue", action="store_true", default=False)
    op.add_option("-r", "--rootpath", action="callback", callback=rootpath_cb, dest="rootPath",
                  default="/mnt/sysimage", nargs=1, type="string")
    op.add_option("-t", "--test", action="store_true", default=False)
    op.add_option("--targetarch", dest="targetArch", nargs=1, type="string")
                  
    # Display
    op.add_option("--headless", dest="isHeadless", action="store_true", default=False)
    op.add_option("--lowres", dest="runres", action="store_const", const="640x480")
    op.add_option("--nofb")
    op.add_option("--resolution", action="callback", callback=resolution_cb, dest="runres",
                  default="800x600", nargs=1, type="string")
    op.add_option("--serial", action="store_true", default=False)
    op.add_option("--usefbx", dest="xdriver", action="store_const", const="fbdev")
    op.add_option("--virtpconsole")
    op.add_option("--vnc", action="store_true", default=False)
    op.add_option("--vncconnect")
    op.add_option("--xdriver", dest="xdriver", action="store", type="string", default=None)

    # Language
    op.add_option("--keymap")
    op.add_option("--kbdtype")
    op.add_option("--lang")

    # Obvious
    op.add_option("--loglevel")
    op.add_option("--syslog")

    op.add_option("--noselinux", dest="selinux", action="store_false", default=True)
    op.add_option("--selinux", action="store_true")

    op.add_option("--nompath", dest="mpath", action="store_false", default=False)
    op.add_option("--mpath", action="store_true")

    op.add_option("--nodmraid", dest="dmraid", action="store_false", default=True)
    op.add_option("--dmraid", action="store_true")

    op.add_option("--noibft", dest="ibft", action="store_false", default=True)
    op.add_option("--ibft", action="store_true")
    op.add_option("--noiscsi", dest="iscsi", action="store_false", default=False)
    op.add_option("--iscsi", action="store_true")

    # Miscellaneous
    op.add_option("--module", action="append", default=[])
    op.add_option("--nomount", dest="rescue_nomount", action="store_true", default=False)
    op.add_option("--updates", dest="updateSrc", action="store", type="string")
    op.add_option("--dlabel", action="store_true", default=False)

    return op.parse_args()

def setVNCFromKickstart(opts):
    from kickstart import pullRemainingKickstartConfig, KickstartError
    from kickstart import VNCHandlers
    from pykickstart.data import KickstartData
    from pykickstart.parser import KickstartParser

    global vncpassword, vncconnecthost, vncconnectport

    try:
	rc = pullRemainingKickstartConfig(opts.ksfile)
    except KickstartError, msg:
	rc = msg
    except:
	rc = _("Unknown Error")

    if rc is not None:
	stdoutLog.critical(_("Error pulling second part of kickstart config: %s!") % rc)
	sys.exit(1)

    # now see if they enabled vnc via the kickstart file. Note that command
    # line options for password, connect host and port override values in
    # kickstart file
    vncksdata = KickstartData()
    ksparser = KickstartParser(vncksdata, VNCHandlers(vncksdata),
                               missingIncludeIsFatal=False)
    ksparser.readKickstart(opts.ksfile)

    if vncksdata.vnc["enabled"]:
	flags.usevnc = 1

	ksvncpasswd = vncksdata.vnc["password"]
	ksvnchost = vncksdata.vnc["host"]
	ksvncport = vncksdata.vnc["port"]

	if vncpassword == "":
	    vncpassword = ksvncpasswd

	if vncconnecthost == "":
	    vncconnecthost = ksvnchost

	if vncconnectport == "":
	    vncconnectport = ksvncport

    if vncksdata.displayMode!=None:
        flags.vncquestion = False

    return vncksdata.vnc

def setupPythonPath():
    # For anaconda in test mode
    if (os.path.exists('isys')):
        sys.path.append('isys')
        sys.path.append('textw')
        sys.path.append('iw')
    else:
        sys.path.append('/usr/lib/anaconda')
        sys.path.append('/usr/lib/anaconda/textw')
        sys.path.append('/usr/lib/anaconda/iw')

    if (os.path.exists('booty')):
        sys.path.append('booty')
        sys.path.append('booty/edd')
    else:
        sys.path.append('/usr/lib/booty')

    sys.path.append('/usr/share/system-config-date')

def setupTranslations():
    if os.path.isdir("/mnt/source/RHupdates/po"):
        log.info("adding RHupdates/po")
        addPoPath("/mnt/source/RHupdates/po")
    if os.path.isdir("/tmp/updates/po"):
        log.info("adding /tmp/updates/po")
        addPoPath("/tmp/updates/po")
    textdomain("anaconda")

def setupEnvironment():
    # Silly GNOME stuff
    if os.environ.has_key('HOME') and not os.environ.has_key("XAUTHORITY"):
        os.environ['XAUTHORITY'] = os.environ['HOME'] + '/.Xauthority'
    os.environ['HOME'] = '/tmp'
    os.environ['LC_NUMERIC'] = 'C'
    os.environ["GCONF_GLOBAL_LOCKS"] = "1"

    # In theory, this gets rid of our LVM file descriptor warnings
    os.environ["LVM_SUPPRESS_FD_WARNINGS"] = "1"

    # we can't let the LD_PRELOAD hang around because it will leak into
    # rpm %post and the like.  ick :/
    if os.environ.has_key("LD_PRELOAD"):
        del os.environ["LD_PRELOAD"]

def setupLoggingFromOpts(opts):
    if opts.loglevel and logLevelMap.has_key(opts.loglevel):
        log.setHandlersLevel(logLevelMap[opts.loglevel])

    if opts.syslog:
        if opts.syslog.find(":") != -1:
            (host, port) = opts.syslog.split(":")
            logger.addSysLogHandler(log, host, port=int(port))
        else:
            logger.addSysLogHandler(log, opts.syslog)

def getInstClass(opts):
    # if we're not doing a kickstart install, figure out instClass from args
    if opts.ksfile:
        from kickstart import Kickstart
        return Kickstart(opts.ksfile, opts.serial)
    else:
        from installclass import DefaultInstall, availableClasses
        retval = DefaultInstall(flags.expert)

        allavail = availableClasses(showHidden = 1)
        avail = availableClasses(showHidden = 0)
        if len(avail) == 1:
            (cname, cobject, clogo) = avail[0]
            log.info("%s is only installclass, using it" %(cname,))
            retval = cobject(flags.expert)
        elif len(allavail) == 1:
            (cname, cobject, clogo) = allavail[0]
            log.info("%s is only installclass, using it" %(cname,))
            retval = cobject(flags.expert)

        return retval

# ftp installs pass the password via a file in /tmp so
# ps doesn't show it
def expandFTPMethod(opts):
    filename = opts.method[1:]
    opts.method = open(filename, "r").readline()
    opts.method = opts.method[:len(opts.method) - 1]
    os.unlink(filename)

def runVNC(vncpassword, vncconnecthost, vncconnectport, vncStartedCB=None):
    # dont run vncpassword if in test mode
    if flags.test:
	vncpassword = ""

    vnc.startVNCServer(vncpassword=vncpassword,
		       vncconnecthost=vncconnecthost,
		       vncconnectport=vncconnectport,
                       vncStartedCB=vncStartedCB)

    child = os.fork()
    if child == 0:
        for p in ('/mnt/source/RHupdates/pyrc.py', \
                '/tmp/updates/pyrc.py', \
                '/usr/lib/anaconda-runtime/pyrc.py'):
            if os.access(p, os.R_OK|os.X_OK):
                os.environ['PYTHONSTARTUP'] = p
                break

	while 1:
	    print _("Press <enter> for a shell")
	    sys.stdin.readline()
            iutil.execConsole()

def checkMemory(opts):
    if iutil.memInstalled() < isys.MIN_RAM:
        from snack import SnackScreen, ButtonChoiceWindow

        screen = SnackScreen()
        ButtonChoiceWindow(screen, _('Fatal Error'),
                            _('You do not have enough RAM to install %s '
                              'on this machine.\n'
                              '\n'
                              'Press <return> to reboot your system.\n')
                           %(product.productName,),
                           buttons = (_("OK"),))
        screen.finish()
        sys.exit(0)

    # override display mode if machine cannot nicely run X
    if not flags.test:
        if opts.display_mode not in ('t', 'c') and iutil.memInstalled() < isys.MIN_GUI_RAM:
            stdoutLog.warning(_("You do not have enough RAM to use the graphical "
                                "installer.  Starting text mode."))
            opts.display_mode = 't'
            time.sleep(2)

def probeHW(opts, x_already_set, xserver):
    if not opts.isHeadless:
        #
        # Probe what is available for X and setup a hardware state
        #
        # try to probe interesting hw
        skipmouseprobe = not (not os.environ.has_key('DISPLAY') or flags.setupFilesystems)
        xserver.probeHW(skipMouseProbe=skipmouseprobe, forceDriver=opts.xdriver)

        # if the len(videocards) is zero, then let's assume we're isHeadless
        if len(xserver.videohw.videocards) == 0:
            stdoutLog.info (_("No video hardware found, assuming headless"))
            opts.isHeadless = 1
        else:
            # setup a X hw state for use later with configuration.
            try:
                xserver.setHWState()
            except Exception, e:
                stdoutLog.error (_("Unable to instantiate a X hardware state object."))

        # keyboard
        xserver.keyboard = keyboard.Keyboard()
        if opts.keymap:
            xserver.keyboard.set(opts.keymap)

    # floppy
    return floppy.probeFloppyDevice()

def setupGraphicalLinks():
    for i in ( "imrc", "im_palette.pal", "gtk-2.0", "pango", "fonts",
	       "fb.modes"):
        try:
	    if os.path.exists("/mnt/runtime/etc/%s" %(i,)):
	        os.symlink ("../mnt/runtime/etc/" + i, "/etc/" + i)
        except:
	    pass

class Anaconda:
    def __init__(self):
        self.intf = None
        self.dir = None
        self.id = None
        self.method = None
        self.methodstr = None
        self.backend = None
        self.rootPath = None
        self.dispatch = None
        self.isKickstart = False
        self.rescue_mount = True
        self.rescue = False
        self.updateSrc = None
        self.canReIPL = False
        self.reIPLMessage = None

    def setDispatch(self):
        self.dispatch = dispatch.Dispatcher(self)

    def setInstallInterface(self, display_mode):
        # setup links required by graphical mode if installing and verify display mode
        if display_mode == 'g':
            stdoutLog.info (_("Starting graphical installation..."))
            if not flags.test and flags.setupFilesystems:
                setupGraphicalLinks()

            try:
                from gui import InstallInterface
            except Exception, e:
                stdoutLog.error("Exception starting GUI installer: %s" %(e,))
                if flags.test:
                    sys.exit(1)
                # if we're not going to really go into GUI mode, we need to get
                # back to vc1 where the text install is going to pop up.
                if not x_already_set:
                    isys.vtActivate (1)
                stdoutLog.warning("GUI installer startup failed, falling back to text mode.")
                display_mode = 't'
                if 'DISPLAY' in os.environ.keys():
                    del os.environ['DISPLAY']
                time.sleep(2)

        if display_mode == 't':
            from text import InstallInterface
            if not os.environ.has_key("LANG"):
                os.environ["LANG"] = "en_US.UTF-8"

        if display_mode == 'c':
            from cmdline import InstallInterface

        self.intf = InstallInterface()

    def setMethod(self):
        if self.methodstr.startswith('cdrom://'):
            from image import CdromInstallMethod
            self.method =  CdromInstallMethod(self.methodstr, self.rootPath, self.intf)
        elif self.methodstr.startswith('nfs:/'):
            from image import NfsInstallMethod
            self.method =  NfsInstallMethod(self.methodstr, self.rootPath, self.intf)
        elif self.methodstr.startswith('nfsiso:/'):
            from image import NfsIsoInstallMethod
            self.method =  NfsIsoInstallMethod(self.methodstr, self.rootPath, self.intf)
        elif self.methodstr.startswith('ftp://') or self.methodstr.startswith('http://'):
            from urlinstall import UrlInstallMethod
            self.method =  UrlInstallMethod(self.methodstr, self.rootPath, self.intf)
        elif self.methodstr.startswith('hd://'):
            from harddrive import HardDriveInstallMethod
            self.method =  HardDriveInstallMethod(self.methodstr, self.rootPath, self.intf)
        else:
            self.method =  None

if __name__ == "__main__":
    anaconda = Anaconda()

    setupPythonPath()

    # Allow a file to be loaded as early as possible
    try:
        import updates_disk_hook
    except ImportError:
        pass

    # Set up logging as early as possible.
    import logging
    from anaconda_log import logger, logLevelMap

    log = logging.getLogger("anaconda")
    stdoutLog = logging.getLogger("anaconda.stdout")

    # pull this in to get product name and versioning
    import product

    # this handles setting up RHupdates for pypackages to minimize the set needed
    setupPythonUpdates()

    import signal, traceback, string, isys, iutil, time
    from exception import handleException
    import dispatch
    import warnings
    import rhpl
    import vnc
    import users
    from flags import flags
    from rhpl.translate import _, textdomain, addPoPath

    if rhpl.getArch() != "s390" and os.access("/dev/tty3", os.W_OK):
        logger.addFileHandler ("/dev/tty3", log)

    warnings.showwarning = AnacondaShowWarning

    setupTranslations()

    # reset python's default SIGINT handler
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGSEGV, isys.handleSegv)

    setupEnvironment()

    # we need to do this really early so we make sure its done before rpm
    # is imported
    iutil.writeRpmPlatform()

    extraModules = []               # XXX: this would be better as a callback
    runres_override = False
    graphical_failed = 0
    instClass = None                # the install class to use
    vncpassword = ""
    vncconnecthost = ""
    vncconnectport = ""
    xserver_pid = None

    (opts, args) = parseOptions()

    # Now that we've got arguments, do some extra processing.
    instClass = getInstClass(opts)

    setupLoggingFromOpts(opts)

    anaconda.rootPath = opts.rootPath
    # Default is to prompt to mount the installed system.
    anaconda.rescue_mount = not opts.rescue_nomount

    if opts.dlabel: #autodetected driverdisc in use
        flags.dlabel = True

    if opts.noipv4:
        flags.useIPv4 = False

    if opts.noipv6:
        flags.useIPv6 = False

    if opts.updateSrc:
        anaconda.updateSrc = opts.updateSrc

    if opts.method:
        anaconda.methodstr = opts.method

    if opts.method:
        if opts.method[0] == '@':
            expandFTPMethod(opts)

        anaconda.methodstr = opts.method

    if opts.module:
        for mod in opts.module:
            (path, name) = string.split(mod, ":")
            extraModules.append((path, name))

    if opts.test:
        flags.test = 1
        flags.setupFilesystems = 0

    if opts.vnc:
        flags.usevnc = 1
        opts.display_mode = 'g'
        vncpassword = vnc.getVNCPassword()

    if opts.vncconnect:
        cargs = string.split(opts.vncconnect, ":")
        vncconnecthost = cargs[0]
        if len(cargs) > 1:
            if len(cargs[1]) > 0:
                vncconnectport = cargs[1]

    if opts.ibft:
        flags.ibft = 1

    if opts.iscsi:
        flags.iscsi = 1

    if opts.targetArch:
        flags.targetarch = opts.targetArch

    # set dmraid and mpath flags 
    flags.dmraid = opts.dmraid
    flags.mpath = opts.mpath

    if opts.serial:
        flags.serial = True
    if opts.virtpconsole:
        flags.virtpconsole = opts.virtpconsole

    # probing for hardware on an s390 seems silly...
    if rhpl.getArch() == "s390":
        opts.isHeadless = True

    if not flags.test and not flags.rootpath:
        isys.auditDaemon()

    users.createLuserConf(anaconda.rootPath)

    # setup links required for all install types
    # list of 3-tuples:  ([file list], sourcepath, destpath):
    links = [(["services", "protocols", "nsswitch.conf", "joe", "selinux",
               "mke2fs.conf", "multipath.conf", "yum"],
              "/mnt/runtime/etc/", "/etc/"),
             (["multipath", "kpartx", "dmsetup", "dmraid"],
              "/mnt/runtime/usr/sbin/", "/sbin/"),
             (["scsi_id"], "/mnt/runtime/lib/udev/", "/sbin/")]

    for (files, source, dest) in links:
        for i in files:
            try:
                if os.path.exists(source + i):
                    os.symlink (".." + source + i, dest + i)
            except:
                pass

    for i in os.listdir("/mnt/runtime/usr/sbin"):
        if i.startswith('mpath_prio_'):
            os.symlink ("../mnt/runtime/usr/sbin/" + i, "/sbin/" + i)

    #
    # must specify install, rescue mode
    #
    if opts.rescue:
        anaconda.rescue = True

        if not anaconda.methodstr:
            sys.stderr.write('--method required for rescue mode\n')
            sys.exit(1)

        import rescue, instdata

        iutil.makeDriveDeviceNodes()
        iutil.makeCharDeviceNodes()

        anaconda.id = instdata.InstallData(anaconda, [], "fd0", anaconda.methodstr, opts.display_mode)
        rescue.runRescue(anaconda)

        # shouldn't get back here
        sys.exit(1)
    else:
        if not anaconda.methodstr:
            sys.stderr.write('no install method specified\n')
            sys.exit(1)

    #
    # Here we have a hook to pull in second half of kickstart file via https
    # if desired.
    #
    if opts.ksfile:
        anaconda.isKickstart = True
        vncksdata = setVNCFromKickstart(opts)

        if vncksdata["enabled"]:
            opts.display_mode = 'g'

    #
    # Determine install method - GUI or TUI
    #
    # use GUI by default except for install methods that were traditionally
    # text based due to the requirement of a small stage 2
    #
    # if display_mode wasnt set by command line parameters then set default
    #
    if not opts.display_mode:
        if (anaconda.methodstr and 
            anaconda.methodstr.startswith('ftp://') or
            anaconda.methodstr.startswith('http://')):
            opts.display_mode = 't'
        else:
            opts.display_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion=lay_mode = 'g'
    
    #we prefer vnc over text mode, so askion