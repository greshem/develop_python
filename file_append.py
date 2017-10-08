#!/usr/bin/python 
stuff='''
set shiftwidth=4
set tabstop=4
set expandtab
set noswapfile
syntax on
''';

fh = open("/etc/vimrc", 'a')
fh.write(stuff)


