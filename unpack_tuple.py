#!/use/bin/python

def  return_four_value():
    return (1,2,3,4,5);

def  return_zeor_value():
    return (1,2);

#a,b,c,d,e= return_four_value();
#a,b,c,d,e,f= return_four_value();

#ValueError: need more than 0 values to unpack
a,b,c,d,e,f= ()

#bb,bbb = return_zeor_value();
