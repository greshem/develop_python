#coding=utf-8
# wc *.py   |sort -n  |more
import os;

#snippet #!
#	#!/usr/bin/env python
#	# -*- coding: utf-8 -*-

def append_file_to_snippets_DB(python_file):
    name=os.path.basename(python_file);
    fh = open("/root/bin/snippets/python.snippets", 'a')
    fh.write("snippet %s\n"%(name) );
    fh.write("\t#-----snippet %s start ----\n"%(name) );

    src_file=open(python_file);
    for line in src_file.readlines():
        fh.write("\t%s"%(line) )

    fh.close();



""""
本地目录下  小于20行的代码, 做成snippet
"""
def  get_python_snippet_list(exists_snippet):

    import commands
    buffers =commands.getoutput("  wc *.py   |sort -n   ");
    output=buffers.split("\n");
    for each in output:

        array=each.split();
        if int(array[0]) <=20:
            pass;
            #print "%s -> %s 小于20行  should  append to snippet "%(array[0],array[3]);
        else:
            #print "%s -> %s 大于20行  跳过 "%(array[0],array[3]);
            continue;
        
        filename=array[3] 
        name=array[3];
        name=os.path.basename(name);
        name_py=os.path.basename(name);
        name=name.replace(".py","");
        if name in  exists_snippet or  name_py  in exists_snippet  :
            pass
            #print "name: %s  snippet 已经存在"%name;
        else:
            print "#开始添加文件:%s 到DB中 "%filename;
            append_file_to_snippets_DB(filename);

             
         

""""
获取已经存在的 snippets的名字
"""
def get_snippet_name():
    keywords=[];
    fh=open("/root/bin/snippets/python.snippets");
    for line in fh.readlines():
        if line.startswith("snippet"):
            array=line.split();
            #print line;
            #print array[1];
            keywords.append(array[1]);
    return keywords;

    
snippet_list=get_snippet_name();
get_python_snippet_list(snippet_list);

