#
# userauth_text.py: text mode authentication setup dialogs
#
# Copyright 2000-2002 Red Hat, Inc.
#
# This software may be freely redistributed under the terms of the GNU
# library public license.
#
# You should have received a copy of the GNU Library Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#


from snack import *
#from constants_text import *
from rhpl.translate import _

import rhpl
import os
import sys


def has_bad_chars(pw):
    allowed = string.digits + string.ascii_letters + string.punctuation + " "
    for letter in pw:
        if letter not in allowed:
            return 1
    return 0

class RootPasswordWindow:
    def __call__ (self, screen):
        toplevel = GridFormHelp (screen, _("Root Password"), "rootpw", 1, 3)

        toplevel.add (TextboxReflowed(37, _("Pick a root password. You must "
				"type it twice to ensure you know "
				"what it is and didn't make a mistake "
				"in typing. Remember that the "
				"root password is a critical part "
				"of system security!")), 0, 0, (0, 0, 0, 1))


        entry1 = Entry (24, password = 1, text = "password")
        entry2 = Entry (24, password = 1, text = "password")
        passgrid = Grid (2, 2)
        passgrid.setField (Label (_("Password:")), 0, 0, (0, 0, 1, 0), anchorLeft = 1)
        passgrid.setField (Label (_("Password (confirm):")), 0, 1, (0, 0, 1, 0), anchorLeft = 1)
        passgrid.setField (entry1, 1, 0)
        passgrid.setField (entry2, 1, 1)
        toplevel.add (passgrid, 0, 1, (0, 0, 0, 1))
        
        #bb = ButtonBar (screen, (TEXT_OK_BUTTON, TEXT_BACK_BUTTON))
        bb = ButtonBar (screen, ("OK", "BACK"))
        toplevel.add (bb, 0, 2, growx = 1)

        while 1:
            toplevel.setCurrent (entry1)
            result = toplevel.run ()
            rc = bb.buttonPressed (result)
            if rc == TEXT_BACK_CHECK:
                screen.popWindow()
                return INSTALL_BACK
            if len (entry1.value ()) < 6:
                ButtonChoiceWindow(screen, _("Password Length"),
		       _("The root password must be at least 6 characters "
			 "long."),
		       buttons = [ TEXT_OK_BUTTON ], width = 50)
            elif entry1.value () != entry2.value ():
                ButtonChoiceWindow(screen, _("Password Mismatch"),
		       _("The passwords you entered were different. Please "
			 "try again."),
		       buttons = [ TEXT_OK_BUTTON ], width = 50)
            elif has_bad_chars(entry1.value()):
                ButtonChoiceWindow(screen, _("Error with Password"),
		       _("Requested password contains non-ascii characters "
                         "which are not allowed for use in password."),
		       buttons = [ TEXT_OK_BUTTON ], width = 50)
            else:
                break

            entry1.set ("")
            entry2.set ("")

        screen.popWindow()
        return INSTALL_OK


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

sys.path.append('isys')
sys.path.append('textw')
sys.path.append('iw')
sys.path.append('/usr/lib/anaconda')
sys.path.append('/usr/lib/anaconda/textw')
sys.path.append('/usr/lib/anaconda/iw')
sys.path.append('booty')
sys.path.append('booty/edd')
sys.path.append('/usr/lib/booty')
sys.path.append('/usr/share/system-config-date')



screen = SnackScreen()
a=RootPasswordWindow();
a.__call__(screen);
