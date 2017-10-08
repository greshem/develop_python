#coding=utf-8

import random;
import string;
def GB2312():
	head = random.randint(0xB0, 0xCF)
	body = random.randint(0xA, 0xF)
	tail = random.randint(0, 0xF)
	val = ( head << 8 ) | (body << 4) | tail
	str = "%x" % val
	return str.decode('hex');
	#return str.decode('hex').decode('gb2312') 

while 1:
	hz1=GB2312();

	hz2=GB2312();
	hz3=GB2312();
	hz4=GB2312();
	
	path=("%s/%s/%s/%s")%(hz1, hz1+hz2, hz1+hz2+hz3, hz1+hz2+hz3+hz4);
	print path;

	#tmp="ÖÐ¹ú"
	#print unicode(tmp, "gb2312");
	#print tmp;
