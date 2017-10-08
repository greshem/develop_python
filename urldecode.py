#!/usr/bin/python

'''
urldecode.py

Copyright 2006 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

'''

import urllib
import sys
import getopt
try:
    import core.controllers.outputManager as om
except:
    class om:
        class out:
            def information( str ):
                print '\r' + str
            information = staticmethod(information)

def usage():
    om.out.information('w3af - urldecoder')
    om.out.information('')
    om.out.information('Options:')
    om.out.information('    -h  Print this help message.')
    om.out.information('    -d  String to be decoded.')
    om.out.information('')
    om.out.information('Example: urldecode -d decodeMeNow')
    
def main():
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:", ["help", "decode"])
    except getopt.GetoptError:
        # print help information and exit:
        usage()
        sys.exit(2)
    decode = None
    for o, a in opts:
        if o in ("-d", "--decode"):
            decode = a
        if o in ("-h", "--help"):
            usage()
            sys.exit()

    if decode == None:
            usage()
            sys.exit()
    else:
        om.out.information( urllib.unquote_plus( decode ) )
        
if __name__ == "__main__":
  main()
  
