import paramiko

class my_ssh():
    def connect(self, ip, port, user_name, passwd):
        self.ip = ip
        self.user_name = user_name
        self.passwd = passwd
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.load_system_host_keys()
        self.ssh.connect(ip, port, user_name, passwd, timeout = 5)
        #self.scp = scp.SCPClient(self.ssh.get_transport())

    def ssh_execute(self,cmd):
        cmd += " 2>&1"
        print "ssh request: [{0}]".format(cmd)
        stdin, stdout, stderr =  self.ssh.exec_command(cmd)
        outlines = stdout.readlines()
        if len(outlines) != 0:
            print "ssh response: [{0}]".format("".join(outlines))
        return outlines


    #def execute(self, cmd):
    #    return self.ssh.exec_command(cmd)

if __name__=="__main__":
    ssh=my_ssh();
    #ssh.connect("192.168.1.100",22, "root", "Emotibot1");
    #ssh.connect("127.0.0.1",7773, "root", "root");
    ssh.connect("10.4.144.223",22, "root", "root");
    buf=ssh.ssh_execute("ifconfig -a ");
    for each in buf:
        print each,

