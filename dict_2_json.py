import  json;

data1 = {'b':789,'c':456,'a':123}
data2 = {'a':123,'b':789,'c':456}
d1 = json.dumps(data1,sort_keys=True)
d2 = json.dumps(data2)
d3 = json.dumps(data2,sort_keys=True)
d4 = json.dumps(data2, indent=1, sort_keys=True);


print d1
print d2
print d3
print d1==d2
print d4
