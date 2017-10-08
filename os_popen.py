import os;
output=os.popen("cat /etc/passwd");
print output.read();
