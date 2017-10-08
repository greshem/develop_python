def method_1():
    import os;
    output=os.popen("ifconfig");
    ifcfg= output.read();

    array=[word for word in ifcfg.lower().split()]

    print array;

def method_2():
    import commands
    mplayer = commands.getoutput ('which mplayer')
    ifconfig =commands.getoutput(" ifconfig -a ");
    output=ifconfig.split("\n");
    for each in output:
        print each;

if __name__=="__main__":
    #method_2();
    method_1();

