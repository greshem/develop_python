#!/usr/bin/python
class Sing(object):  
    def __init__():  
        "disable the __init__ method" 
 
    __inst = None # make it so-called private 
 
    @staticmethod 
    def getInst():  
        if not Sing.__inst:  
            Sing.__inst = object.__new__(Sing)  
        return Sing.__inst

    name = 'myname'
    def GetName(self):
        return self.name

    def SetName(self, name = ''):
        if name != '':
            self.name = name


if __name__ =='__main__':
    print __name__
    gcb = Sing.getInst()
    print gcb, gcb.GetName()

    gcb.SetName('new name')
   
    gcb1 = Sing.getInst()
    print gcb1, gcb1.GetName()
