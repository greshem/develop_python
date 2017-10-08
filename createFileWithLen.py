#coding:gbk
#!/usr/bin/python
import sys;
import os;

#人类可读的 等同于 ls -la -h 
def humanLen(size):
	size=long(size);
	size_str="";
	if(size <=1024):
		size_str="%d "% ((long(size))); 
	elif((size)> 1024 and long(size) <=1024*1024):
		size_str="%d K"% ((long(size)/1024)); 
	elif  (size> 1024*1024 and size <= 1024*1024*1024):
		size_str="%d M" %  ((long(size)/1024)/1024); 
	elif  (size> 1024*1024*1024 ):
		size_str="%d G" %  (((long(size)/1024)/1024)/1024); 
	
	return size_str;	

# 渲染 一帧  并返回 字符串. 

def getOneFrame():
	pass;

def fill_string(size):
	ret_str=""
	for i in range(0,long(size)-1):
		ret_str+='#';

	ret_str+='\n';
	return ret_str;


def genFileWithLen(dirname, size):
	output="%s/%s"%(dirname, size);
	#注意这里 windows 下假如不是这样的话 wb , 他会自己另外添加一个\r 导致文件 大小 不正确. 
	f=open(output, "wb");
	temp_str="";
	segment=4096;
	count= int(long(size)/4096);
	left = size%4096;
	for i in range(0, count ):
		#print "4096";
		temp_str=fill_string(long(segment));
		f.write("%s"%temp_str);
		#print "str len %d"%len(temp_str);
		
	#print left; 	
	temp_str=fill_string(long(left));
	f.write("%s"%temp_str);
	f.close();


def gen_path_with(size):
    output_dir="%s"%(long(size));
    ret_dir="%s/%s/%s/%s/%s"%( output_dir[0:1], output_dir[0:2], output_dir[0:3], output_dir[0:4], output_dir);
    return ret_dir;
	
	
def bench_nwserv():
	import random;
	import os;
	#os.makedirs("/tmp/aa/bb/cc/ee/ff");
	#pathname = os.path.dirname(sys.argv[0])
	#basename = os.path.basename(sys.argv[0])


	for i in range(0, 65536):
			size =	random.randrange(0, 100000);
			#print size;
			path=gen_path_with( size );
			dirname = os.path.dirname(path);
			basename = os.path.basename(path);
		
			#print "dirname -> %s", dirname;
			if not os.path.isdir(dirname):
				os.makedirs(dirname);
			genFileWithLen(dirname, size);
			#print "basename -> %s", basename;
				
	
#mainloop
########################################################################
if not  os.path.isdir("tmp"):
	os.mkdir("tmp");
os.chdir("tmp");
# if( len(sys.argv) != 2):
# 	print "Usage:	%s  size "%sys.argv[0];
# 	sys.exit(-1);

#文件名和文件大小一样. 
# output=sys.argv[1];
# size=output;
# 
# size_str = humanLen(size); 
# print "OUTPUT FILE %s"% output;
# print "Size %s"% humanLen(size);

#genFileWithLen(long(size));
bench_nwserv()
