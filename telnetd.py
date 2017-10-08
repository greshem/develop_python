import threading  

class myThread(threading.Thread):
    def __init__(self,conn,add):
        threading.Thread.__init__(self)
        self.inputstr = ''
    self.connection=conn
    self.address=add

    def run(self):
    	ii=0
        while True:
			self.connection.settimeout(50)
			buf = self.connection.recv(1024)
        	if  buf.rfind("\n") > -1 :  
                print "**-"+self.inputstr
                self.connection.close() 
                break
            else:  
                self.inputstr+=buf
        		if ii==0:
            		self.connection.send(buf)
        			ii+=1
                continue

            
            

if __name__ == '__main__':  
   import socket  
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.bind(('127.0.0.1', 8014))  
   sock.listen(5)
   while True:  
       try:
           connection,address = sock.accept()
           ithread=myThread(connection,address)
           ithread.start()
       except socket.timeout:  
           print 'time out' 
