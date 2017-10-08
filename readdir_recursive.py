#coding:gbk 
#!/usr/bin/python
import os, sys
# home.zhenliang@gmail.com
# http://t.qq.com/zhenliang
# 获取指定文件夹下所有图片的名字、长和宽

from stat import *
 
import Image
 
PicPathNameList = []
PicWidthList = []
PicHeightList = []
 
def WalkTree(top, callback):
    for f in os.listdir(top):
         
        pathname = os.path.join(top, f)
        mode = os.stat(pathname)[ST_MODE]
         
        if S_ISDIR(mode):
            WalkTree(pathname, callback)
        elif S_ISREG(mode):
			print pathname
			#callback(pathname)
        else:
            print 'Skipping %s' % pathname
 
def GetPicInfo(file):
 
    global PicPathNameList
    global PicWidthList
    global PicHeightList
 
    try:   
        image = Image.open(file)
        PicPathNameList.append(file)     
        PicWidthList.append(image.size[0])
        PicHeightList.append(image.size[1])
    except IOError:
        pass
 
if __name__ == '__main__':
    WalkTree("/root", GetPicInfo)
    print "PicPathNameList Begin"
    print PicPathNameList
    print PicWidthList
    print PicHeightList
    print "PicPathNameList End"
