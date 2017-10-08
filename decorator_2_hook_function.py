def de(f):
    def __call__():
        print '-------------------------------'
        return f()
    return __call__

@de
def func1():
    print 'I am function func1'

@de
def func2():
    print 'I am function func2'

if __name__ =='__main__':
    func1()
    func2()
