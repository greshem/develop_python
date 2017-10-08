#!/usr/bin/python
import sys;
#print sys.argv[0];
argc=len(sys.argv);
if argc != 2:
	print "Usage: %s input_file\n"%(sys.argv[0]);

file_input=sys.argv[1];
all_the_text = open(file_input).read( )     # 
#print all_the_text;

output="%s.py"%(file_input);
fh=open(output, "a+");
buf="""
string=\"\"\"
%s
\"\"\"
print string;
"""%(all_the_text);
fh.write(buf);
print "%s  generated "%output;

