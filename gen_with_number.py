#!/usr/bin/python
#print tmp_str[0:1];
def  gen_path_with(size):
	output_dir="%s"%(long(size%1000));
	ret_dir="%s/%s/%s/%s"%( output_dir[0:1], output_dir[0:2], output_dir[0:3], output_dir[0:3]);
	return ret_dir;


print gen_path_with(8888)
print gen_path_with(9999999)
print gen_path_with(12)
print gen_path_with(1)
