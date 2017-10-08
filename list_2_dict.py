#!/usr/bin/python
a=range(1,100);

b=dict([(each,each*each) for each in a ]);
c=dict(([each,each*each ] for each in a ) );

#数组.
d=[(each,each*each) for each in a ];

#生成的迭代器
e=((each,each*each) for each in a );


#print b;
print type(e);
print e;
for each in e:
    print each;
