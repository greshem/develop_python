import paramiko
import tn_scp
from  tn_ssh_scp_client import  *;

class SSHClient():
    def connect(self, ip, port, user_name, passwd):
        self.ip = ip
        self.user_name = user_name
        self.passwd = passwd
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.load_system_host_keys()
        self.ssh.connect(ip, port, user_name, passwd, timeout = 5)
        self.scp = scp.SCPClient(self.ssh.get_transport())
        
    def get(self,  remote_path, local_path='',
            recursive=False, preserve_times=False):
        self.scp.get(remote_path, local_path, recursive, preserve_times)
        
    def put(self, file, remote_path='.',
            recursive=False, preserve_times=False):
        self.scp.put(file, remote_path, recursive, preserve_times)
    
    def execute(self, cmd):
        return self.ssh.exec_command(cmd)
        


if __name__=="__main__":
    ssh=SSHClient();
    #ssh.connect("192.168.1.100",22, "root", "Emotibot1");
    ssh.connect("127.0.0.1",7773, "root", "root");
    #buf=ssh.execute("uname");
    buf=ssh_execute(ssh, "uname");

    print buf;
