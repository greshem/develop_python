#coding:gbk
#!/usr/bin/python
# 1. 可以随机生成中文 dir , 用来 测试 是不是 utf8 出现的问题. 
# 2. 行情接收机， DBF 文件的堆栈的跟踪.  对于 dbf 文件的  跟踪. 
# 3. nw 里面的 cache 的数据的跟踪, 生成 core-dump 文件 对比有没有 不同， cache 的机制.  
# 4. windows 的磁盘 反应 缓慢的问题. , 判断假如是 windows 的客户端， 不断开连接. 
# 5. 同一个文件名 cache  , inode  变化 下 不同情况下的测试.  
# 6. 跟踪 nwconn 的代码覆盖率，  找出  文件读写 创建时候的 针对代码. 
# 7. mkdir  rename  move 的 压力测试. file 的 rename  dir 的rename, 
# 	F5 对应的函数， 刷新对应的函数，    
# 8. ncp 的   客户端
# 9. dos 的客户端的问题, dos 对文件进行读写 有没有问题. 
#   


import sys;
import os;

#大小变成 人类可读的 string, 等同于 ls -la -h 
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
	for i in range(1,long(size)):
		ret_str+='#';
	#if size!=1:
		
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
	if long(left)>0:
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
			#size =	random.randrange(0, 100000);
			size=i;
			#print size;
			#size=4096;	
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
