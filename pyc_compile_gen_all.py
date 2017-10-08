#!/usr/bin/python
#coding:utf-8
#批量生成pyc文件
#一般来说，我们的工程都是在一个目录下的，一般不会说仅仅编译一个py文件而已，而是需要把整个文件夹下的py文件都编译为pyc文件，python又为了我们提供了另一个模块：compileall 。使用方法如下：
import compileall
compileall.compile_dir(r'/root/bin/develop_python/')
