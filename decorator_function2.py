#!/usr/bin/python 
#coding:utf-8
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped
 
@makebold
@makeitalic
def hello():
    return "hello world"
 
print hello();
#print hello() ## 返回 <b><i>hello world</i></b>
