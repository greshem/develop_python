import os
from os.path import join, getsize

def getdirsize(dir):
   size = 0L
   for root, dirs, files in os.walk(dir):
      size += sum([getsize(join(root, name)) for name in files])
      print join(root,name);
      #print size
   return size

#if '__name__' == '__main__':
filesize = getdirsize('/root/bin/')
print 'There are %.3f' % (filesize/1024/1024), 'Mbytes in /root/bin/'

