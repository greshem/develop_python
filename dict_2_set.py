#!/usr/bin/python

test = dict([(each,each*2) for each in range(1,100)]);

b=set(test);
print b;

c=filter(lambda x:x>80, b);
new_dict=dict([ (each,test[each]) for each in c ]) ;

print new_dict;

