#coding:gbk
#!/usr/bin/python
def fill_string(size):
	ret_str=""
	for i in range(0,long(size)-2):
		ret_str+='#';

	ret_str+='\n';
	return ret_str;

a="";
print fill_string(1024);
