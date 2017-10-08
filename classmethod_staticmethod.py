class  computer:
    @property
    def name(self):
        return "linux_server";

    @property
    def ips(self):
        return ['192.168.1.1', '192.168.1.2'];

    @staticmethod
    def mystatic(wParam,lParam):
        print 'this is  a static method'

    @classmethod
    def newClass(cls):
        return 'class method',cls;


class Rabbit(object):
    def __init__(self,name):
        self._name = name
    @classmethod
    def newClass(cls):
        return 'abc',cls,Rabbit('')
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,newname):
        self._name= newname



four= computer();
print four.name;
print four.ips;
four.mystatic(1,2);
four.mystatic(1,2);
print four.newClass();

computer.mystatic("a","b");
print computer.newClass();
