import Queue
myqueue = Queue.Queue(maxsize = 100000)
for each in range(1,1000):
    myqueue.put(each);

#print  myqueue.qsize();
#print  myqueue.get();

while  not myqueue.empty() :
    print  myqueue.get();
