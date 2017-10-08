def all_members(aClass):
    try:
        #new type class
        mro = list(aClass.__mro__)
    except AttributeError:
        #old type class
        def getmro(aClass,recurse):
#            print 'getmro:',aClass.__name__
            mro = [aClass]
            for base in aClass.__bases__:
                mro.extend(recurse(base,recurse))
            return mro
        def getmro1(aClass):
            mro = [aClass]
            for base in aClass.__bases__:
                mro.extend(getmro1(base))
            return mro
        mro = getmro(aClass,getmro)
#        mro = getmro1(aClass)

    mro.reverse()
    print aClass.__name__," mro:",mro
    members = {}
    for someClass in mro:
        members.update(vars(someClass))
    return members
class A1:
    '''A1 doc'''
    a = 1
class A2(A1):
    '''A2 doc'''
    a = 2
class A3(A2):
    '''A3 doc'''
    a = 3
    
class B1(object):
    '''B1 doc'''
    a = 1
class B2(B1):
    '''B2 doc'''
    a = 2
class B3(B2):
    '''B3 doc'''
    a = 3
    
if __name__ == '__main__':
    print all_members(A3)
    print all_members(B3)