#!/usr/bin/python
# -*- coding: utf-8 -*-
import struct
import os
import sys

#拼音表偏移，
startPy = 0x1540
#汉语词组表偏移
startChinese = 0x2628
#全局拼音表
GPy_Table = {}

#解析结果
#元组(词频,拼音,中文词组)的列表
GTable = []

def byte2str(data):
    '''将原始字节码转为字符串'''
    i = 0
    length = len(data)
    ret = u''
    while i < length:
        x = data[i] + data[i+1]
        t = unichr(struct.unpack('H',x)[0])
        if t == u'\r':
            ret += u'\n'
        elif t != u' ':
            ret += t
        i += 2
    return ret
#获取拼音表
def getPyTable(data):

    if data[0:4] != "\x9D\x01\x00\x00":
        return None
    data = data[4:]
    pos = 0
    length = len(data)
    while pos < length:
        index = struct.unpack('H',data[pos]+data[pos+1])[0]
        #print index,
        pos += 2
        l = struct.unpack('H',data[pos]+data[pos+1])[0]
        #print l,
        pos += 2
        py = byte2str(data[pos:pos+l])
        #print py
        GPy_Table[index]=py
        pos += l

#获取一个词组的拼音
def getWordPy(data):
    pos = 0
    length = len(data)
    ret = u''
    while pos < length:

        index = struct.unpack('H',data[pos]+data[pos+1])[0]
        ret += GPy_Table[index]
        pos += 2
    return ret

#获取一个词组
def getWord(data):
    pos = 0
    length = len(data)
    ret = u''
    while pos < length:

        index = struct.unpack('H',data[pos]+data[pos+1])[0]
        ret += GPy_Table[index]
        pos += 2
    return ret

#读取中文表
def getChinese(data):
    #import pdb
    #pdb.set_trace()

    pos = 0
    length = len(data)
    while pos < length:
        #同音词数量
        same = struct.unpack('H',data[pos]+data[pos+1])[0]
        #print '[same]:',same,

        #拼音索引表长度
        pos += 2
        py_table_len = struct.unpack('H',data[pos]+data[pos+1])[0]
        #拼音索引表
        pos += 2
        # py = getWordPy(data[pos: pos+py_table_len])

        #中文词组
        pos += py_table_len
        for i in xrange(same):
            #中文词组长度
            c_len = struct.unpack('H',data[pos]+data[pos+1])[0]
            #中文词组
            pos += 2
            word = byte2str(data[pos: pos + c_len])
            #扩展数据长度
            pos += c_len
            ext_len = struct.unpack('H',data[pos]+data[pos+1])[0]
            #词频
            pos += 2
            count  = struct.unpack('H',data[pos]+data[pos+1])[0]

            # 保存
            # GTable.append((count,py,word))
            GTable.append(word)
            # 到下个词的偏移位置
            pos += ext_len


def deal(file_name):
    print '-'*60
    f = open(file_name, 'rb')
    data = f.read()
    f.close()


    if data[0:12] != "\x40\x15\x00\x00\x44\x43\x53\x01\x01\x00\x00\x00":
        print "确认你选择的是搜狗(.scel)词库?"
        sys.exit(0)
    #pdb.set_trace()

    print u"词库名：" ,byte2str(data[0x130:0x338])#.encode('GB18030')
    print u"词库类型：" ,byte2str(data[0x338:0x540])#.encode('GB18030')
    print u"描述信息：" ,byte2str(data[0x540:0xd40])#.encode('GB18030')
    # print u"词库示例：",byte2str(data[0xd40:startPy])#.encode('GB18030')
    #
    getPyTable(data[startPy:startChinese])
    getChinese(data[startChinese:])

if __name__ == '__main__':
    #path1 = r'dict/'.replace('\\', '/')
    #path2 = r'/tmp/'.replace('\\', '/')
    #for filename in os.listdir(path1):

    for filename in sys.argv[1:]:
        print filename
        deal(filename)

        # 保存结果
        f = open(filename + '.txt', 'w')
        # 删除相同元素
        GTable_filter = sorted(set(GTable), key=GTable.index)

        for word in GTable_filter:
            f.write(unicode(word).encode('GB18030'))
            f.write('\n')
        f.close()
