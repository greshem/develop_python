#!/usr/bin/python
v=[]
v.append(['1.0.1.4', '1.4.1','1.0.2', '1.0.21', '1.2.9','2.7.1', '1.2.11','2.3.1'])
v.append(['2.3.1','1.0.1.2', '1.4.1','1.2.11','1.0.2', '1.0.21', '1.2.9','2.7.1'])
v.append(['5.0', '1.4','0.2', '1.0.21', '1.2.9','2.7.1', '1.2.11','2.3.1'])
v.append(['1.0.1', '1.0.2', '1.0.21', '1.2.9', '1.2.11'])
v.append([ '1.0.2.11','1.0.2','1.0'])


def addStr(x, y): return x+y

def verCmp(x, y):
    x1 = x.split('.')
    y1 = y.split('.')

    for i in range(min(len(x1), len(y1))):
        maxlen = max(len(x1[i]), len(y1[i]))
        x1[i] = x1[i].rjust(maxlen, '0')
        y1[i] = y1[i].rjust(maxlen, '0')
    return cmp(reduce(addStr, x1), reduce(addStr, y1))

for i in v:
    #print sorted(i, verCmp, reverse=True)
    print sorted(i, verCmp)
