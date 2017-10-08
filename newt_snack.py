#!/usr/bin/python
from snack import SnackScreen, ButtonChoiceWindow
screen = SnackScreen()
ButtonChoiceWindow(screen, ('Fatal Error'),
					('You do not have enough RAM to install %s '
					  'on this machine.\n'
					  '\n'
					  'Press <return> to reboot your system.\n')
				   %("wenshuna",),
				   buttons = (("OK"),))
screen.finish()
