"""GMail file sender: Send a file use GMail. 
"""  
  
from __future__ import with_statement  
import os  
import sys  
from smtplib import SMTP  
from email.MIMEMultipart import MIMEMultipart  
from email.mime.application import MIMEApplication  
import time  
  
if len(sys.argv) < 2:  
    print 'Usage: python %s <file path>' % os.path.basename(sys.argv[0])  
    sys.exit(-1)  
  
config =  {  
    'from': 'qianzhongjie@gmail.com',
    'to': 'qianzhongjie@gmail.com',  
    'subject': '[gsend]Send file %s' % sys.argv[1],  
    'file': sys.argv[1],  
    'server': 'smtp.gmail.com',  
    'port': 587,  
    'username': 'qianzhongjie@gmail.com',  
    'password': 'qianqian',  
}  
  
print 'Preparing...',  
  
message = MIMEMultipart( )  
message['from'] = config['from']  
message['to'] = config['to']  
message['Reply-To'] = config['from']  
message['Subject'] = config['subject']  
message['Date'] = time.ctime(time.time())  
  
message['X-Priority'] =  '3'  
message['X-MSMail-Priority'] =  'Normal'  
message['X-Mailer'] =  'Microsoft Outlook Express 6.00.2900.2180'  
message['X-MimeOLE'] =  'Produced By Microsoft MimeOLE V6.00.2900.2180'  
  
with open(config['file'], 'rb') as f:  
    file = MIMEApplication(f.read())  
file.add_header('Content-Disposition', 'attachment', filename=os.path.basename(config['file']))  
message.attach(file)  
  
print 'OK'  
print 'Logging...',  
  
smtp = SMTP(config['server'], config['port'])  
smtp.ehlo()  
smtp.starttls()  
smtp.ehlo()  
smtp.login(config['username'], config['password'])  
  
print 'OK'  
print 'Sending...',  
  
smtp.sendmail(config['from'], [config['from'], config['to']], message.as_string())  
  
print 'OK'  
  
smtp.close()  
  
time.sleep(1)  
