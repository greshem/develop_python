#!/usr/bin/env python2.0

import sys, re
from htmlentitydefs import entitydefs

entre=re.compile('&([a-zA-Z0-9]+|#[0-9]+|#x[a-zA-Z0-9]+);')
spre=re.compile('[\s,.:;!\?]+',re.I|re.S|re.M)
htre=re.compile('</?[^>]+>')

def confents(text):
	res=''
	while len(text)>0:
		m=entre.search(text)
		if m is not None:
			res+=text[:m.start()]
			text=text[m.end():]
			if m.group(1)[:2]=='#x':
				ent=atoi(m.group(1)[2:],16)
			elif m.group(1)[0]=='#':
				ent=atoi(m.group(1)[1:])
			else:
				if entitydefs.has_key(m.group(1)):
					try:
						ent=ord(entitydefs[m.group(1)])
					except:
						ent=ord('?')
				else:
					ent=ord('?')
			if ent<256:
				res+=chr(ent)
			else:
				res+='?'
		else:
			res+=text
			text=''
	return res

def wordList(name, inf, ouf):
	try:
		title=confents(open(name+'.title','r').read().strip())
	except IOError:
		title=''
	text=confents(inf.read())
	ouf.write('*|*T=%s*|**|*%d\n'%(title,len(text)))
	for w in spre.split(title):
		if len(w)>2:
			ouf.write('%s,15,1\n'%(w))
	for w in spre.split(htre.sub(' ',text)):
		if len(w)>2:
			ouf.write('%s\n'%(w))

if __name__=='__main__':
	if len(sys.argv)==3:
		inFile=open(sys.argv[1],'r')
		outFile=open(sys.argv[2],'w')
	elif len(sys.argv)==2:
		inFile=open(sys.argv[1],'r')
		outFile=sys.stdout
	else:
		sys.stderr.write('Usage: arcfilter.py INFILE [OUTFILE]\n')
		sys.exit(1)
	wordList(sys.argv[1],inFile,outFile)
