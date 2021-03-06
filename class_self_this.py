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
    
    def __init__(me):
        """
        Class constructor
        """
        pass


    def warning(me, string):
        """
        Method to print a message as a warning
        Args:
          string [STRING] : the message

        Returns: None
        """

        msg = "%s WARNING: %s" % (me.getTimeStamp(),
                                  string)
        print msg

    
    def info(me, string):
        """
        Method to print a message as a info msg
        Args:
          string [STRING] = the message

        Returns: None
        """
        msg = "%s INFO: %s" % (me.getTimeStamp(),
                                  string)
        print msg
    

    def error(me, string):
        """
        Method to print a message as a error msg
        Args:
          string [STRING] = The message

        Returns: None
        """
        msg = "%s ERROR: %s" % (me.getTimeStamp(),
                                  string)
        print msg
    

    def fatal(me, string):
        """
        Method to print a message as a fatal msg
        Args:
          string [STRING] = The message

        Returns: None
        """
        msg = "%s FATAL: %s" % (me.getTimeStamp(),
                                  string)
        print msg


    def getTimeStamp(me):
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

