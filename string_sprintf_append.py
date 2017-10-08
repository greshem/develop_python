__version = "--== Version ==--\n" \
            "unpyc v%s (testing)\n" % __version__

__help = "--== Help ==--\n" \
	 + __usage + \
	 "d  - disassemble\n" \
	 "x  - show xref`s (used with d)\n" \
	 "v  - verbose (used with d)\n" \
	 "vv - very verbose (used with d)\n" \
	 "D  - decompile (not implemented yet)\n" \
	 "g  - gui (control flows)\n" \
	 "c  - copyright\n" \
	 "V  - version\n" \
	 "h  - help\n" 

__doc__ = """
UnPyc - program for disassembling and decompiling *.pyc files.

`./UnPyc cVh`::
%s
%s
%s
""" % tuple(map(lambda x:re.compile(r'^',re.M).sub(' ',x),(__copyright,__version,__help))) # for epydoc to be ok
