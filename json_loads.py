#!/usr/bin/python
#coding=utf-8
import json;

def   seg_str():
    import commands
    output = commands.getoutput ("curl -s   http://192.168.1.11:9100/nlp?text=我好饿 ")
    print "|%s|"%(output );
    a=json.loads(output);
    #a=json.loads('{"seg":"我 好 饿","keyword":"好 饿"}');
    print a;
    print a['seg'];

seg_str();
