import datetime
import time;
timestamp=time.time();
print timestamp;
#date=datetime.datetime.utcfromtimestamp(timestamp)

date=datetime.datetime.fromtimestamp(1497512000)
print date;

#1497512137.57
#1497512000



print date;


#epoch,shortterm,midterm,longterm
#1492617415.526,0.210000,0.180000,0.150000
for each in  open("/var/lib/collectd/csv/gresrv/load/load-2017-04-19").readlines():
    #print each,
    if each.startswith("epoch"):
        continue;

    line=each.split(",")
    date=datetime.datetime.fromtimestamp(float(line[0]))
    print date;
    
