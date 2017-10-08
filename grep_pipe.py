import commands
mplayer = commands.getoutput ('grep port= /root/bin/daemon/ssh_nat/ssh_phabricator.pl')
print mplayer;
