#2011_01_22_ add by greshem
#!/usr/bin/env python  
  
# to delete all cvs directory of a root directory.  
  
import os, string  
  
def deltree(top):  
  for root, dirs, files in os.walk(top, topdown=False):  
    for name in files:  
      os.remove(os.path.join(root, name))  
    for name in dirs:  
      os.rmdir(os.path.join(root, name))  
  os.rmdir(top)  
  
  
def delallcvs(top):  
  for root, dirs, files in os.walk(top, topdown=True):  
    if 'CVS' in dirs:  
      deltree(os.path.join(root, 'CVS'))  
  
  
  
if __name__=='__main__':  
  dir =  os.listdir('.')  
  if 'CVS' in dir:  
    print '--get it!--', os.curdir  
  
    delallcvs(os.curdir)  
  else:  
    print 'can''t get it!'  

