
def h():  
    print 'To be brave'  
    yield 5  
    yield 6
    yield 7

for each in h(): 
    print each;
