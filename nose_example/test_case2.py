
import nose  
from temperature import to_celsius  

def test_freezing():  
    assert to_celsius(32) == 0  

def test_boiling():  
    assert to_celsius(212) == 100  

def test_roundoff():  
    assert to_celsius(100) == 38  

if __name__ == '__main__':  
    nose.runmodule()  
