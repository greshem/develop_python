
import subprocess

vncconfigcommand = ["cat", "/etc/passwd" ]
vncconfo = subprocess.Popen(vncconfigcommand)# we dont want output
print vncconfo.returncode

