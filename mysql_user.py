import MySQLdb
import smtplib
import socket
import sys
from time import strftime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
	conn = MySQLdb.connect (host = "localhost",
    	                    user = "root",
        	                passwd = "qianqian",
            	            db = "mysql")
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)



cursor = conn.cursor()
cursor.execute("SELECT * FROM user")
rows = cursor.fetchall()
for row in rows:
    print type(row);
    print row;

