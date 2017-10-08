###################################################
# Application : AL                                #
#  * Program to quickly launch other programs     #
#                                                 #
# Author      : Rune Devik                        #
# Date        : 16:55 04.30.2006                  #
# License     : GNU General Public License (GPL)  #
###################################################

# Import standard modules
import time
import os.path
import os

class Logger:
    """
    The class implementing the logger
    """
    
    def __init__(self):
        """
        Class constructor
        """
        pass


    def warning(self, string):
        """
        Method to print a message as a warning
        Args:
          string [STRING] : the message

        Returns: None
        """

        msg = "%s WARNING: %s" % (self.getTimeStamp(),
                                  string)
        print msg

    
    def info(self, string):
        """
        Method to print a message as a info msg
        Args:
          string [STRING] = the message

        Returns: None
        """
        msg = "%s INFO: %s" % (self.getTimeStamp(),
                                  string)
        print msg
    

    def error(self, string):
        """
        Method to print a message as a error msg
        Args:
          string [STRING] = The message

        Returns: None
        """
        msg = "%s ERROR: %s" % (self.getTimeStamp(),
                                  string)
        print msg
    

    def fatal(self, string):
        """
        Method to print a message as a fatal msg
        Args:
          string [STRING] = The message

        Returns: None
        """
        msg = "%s FATAL: %s" % (self.getTimeStamp(),
                                  string)
        print msg


    def getTimeStamp(self):
        """
        Method to get a timestamp to be used in
        the log message.
        Args:
          None

        Returns: [STRING] The timestamp
        """
        
        return time.strftime("%m.%d.%y %H:%M:%S ",time.localtime())

a=Logger();

a.warning("[Logger]");
a.info("[Logger]");
a.error("[Logger]");
a.fatal("[Logger]");
a.getTimeStamp();

