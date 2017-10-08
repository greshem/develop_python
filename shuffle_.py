import random
fh=open("/etc/passwd");
lines=fh.readlines();
random.shuffle(lines);
for line in lines:
    print line
