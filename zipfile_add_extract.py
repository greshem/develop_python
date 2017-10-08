#coding:gbk
#Zipping a file:
#
#2011_01_21_ add by greshem
# 或者 python zipfile.py -l file.zip  也可以的. 
import os;
import zipfile
import time;
import glob;
import time;

def getTimeStamp():
    """
    Method to get a timestamp to be used in
    the log message.
    Args:
      None

    Returns: [STRING] The timestamp
    """

    #return time.strftime("%m.%d.%y %H:%M:%S ",time.localtime())
    return time.strftime("%Y-%m-%d",time.localtime())


def get_dir_list(path):
	filelist=[];
	cur=time.time();
	for root, dirs, files in os.walk(path):
		for file in files:
			abs_path = os.path.join(root,file)
			#print "%s" %abs_path;
			mtime = os .path.getmtime(abs_path) ;
			if (cur-mtime) < 24*60*60:
				filelist.append(abs_path);
	return filelist;

def glob_cur_dir():	
	list=[];
	for file in glob.glob("*"):
	#if os.path.isdir(file):
		if os.path.isfile(file):
        	#print(file)
			list.append(file);
	return list;


#list=get_dir_list(".");
list=glob_cur_dir();

output="c:/%s.zip"%getTimeStamp();
f = zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED)
for file in list:
	print file;
	f.write(file)
	
f.close()

#Replace 'w' with 'a' to add files to the zip archive.

#Unzipping all files from a zip archive:
#import zipfile
#zfile = zipfile.ZipFile('archive.zip','r')
#for filename in zfile.namelist():
#    data = zfile.read(filename)
#    file = open(filename, 'w+b')
#    file.write(data)
#    file.close()
