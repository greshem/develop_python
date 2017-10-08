#!/usr/bin/env python
# coding: gbk

# from: http://linuxtoy.org/files/pyip.py
# Blog: http://linuxtoy.org/archives/python-ip.html
#2011_01_10_17:16:55 add by greshem
# H:\_x_file\frequent_\qqwry.rar �ļ������ж�Ӧ�����ݿ⡣

'''��Python�ű���ѯ����IP��

QQWry.Dat�ĸ�ʽ����:

+----------+
|  �ļ�ͷ  |  (8�ֽ�)
+----------+
|  ��¼��  | ����������
+----------+
|  ������  | ����С���ļ�ͷ������
+----------+

�ļ�ͷ��4�ֽڿ�ʼ����ƫ��ֵ+4�ֽڽ�β����ƫ��ֵ

��¼���� ÿ��IP��¼��ʽ ==> IP��ַ[������Ϣ][������Ϣ]

   ���ڹ��Ҽ�¼�����������ֱ�ʾ��ʽ��

       �ַ�����ʽ(IP��¼��5�ֽڲ�����0x01��0x02�����)��
       �ض���ģʽ1(��5�ֽ�Ϊ0x01),�������3�ֽ�Ϊ������Ϣ�洢�ص�ƫ��ֵ
       �ض���ģʽ(��5�ֽ�Ϊ0x02),
   
   ���ڵ�����¼�����������ֱ�ʾ��ʽ�� �ַ�����ʽ���ض���

   ���һ�������ض���ģʽ1�Ĺ��Ҽ�¼���ܸ�������¼

�������� ÿ��������¼��ʽ ==> 4�ֽ���ʼIP��ַ + 3�ֽ�ָ��IP��¼��ƫ��ֵ

   ��������IP����ָ��ļ�¼��һ����¼�е�IP����һ��IP��Χ����ѯ��Ϣ�����
   ��Χ��IP����Ϣ

'''

import sys
import socket
from struct import pack, unpack

class IPInfo(object):
    '''QQWry.Dat���ݿ��ѯ���ܼ���
    '''
    def __init__(self, dbname):
        ''' ��ʼ���࣬��ȡ���ݿ�����Ϊһ���ַ�����
        ͨ����ʼ8�ֽ�ȷ�����ݿ��������Ϣ'''
        
        self.dbname = dbname
        f = file(dbname, 'r')
        self.img = f.read()
        f.close()

        # QQWry.Dat�ļ��Ŀ�ʼ8�ֽ���������Ϣ,ǰ4�ֽ��ǿ�ʼ������ƫ��ֵ��
        # ��4�ֽ��ǽ���������ƫ��ֵ��
        (self.firstIndex, self.lastIndex) = unpack('II', self.img[:8])
        # ÿ��������7�ֽڣ�����õ������ܸ���
        self.indexCount = (self.lastIndex - self.firstIndex) / 7 + 1
	
    def getString(self, offset = 0):
        ''' ��ȡ�ַ�����Ϣ������"����"��Ϣ��"����"��Ϣ

        QQWry.Dat�ļ�¼��ÿ����Ϣ����һ����'\0'��β���ַ���'''
        
        o2 = self.img.find('\0', offset)
        #return self.img[offset:o2]
        # �п���ֻ�й�����Ϣû�е�����Ϣ��
        gb2312_str = self.img[offset:o2]
        try:
            utf8_str = unicode(gb2312_str,'gb2312').encode('utf-8')
        except:
            return 'δ֪'
        return utf8_str

    def getLong3(self, offset = 0):
        '''QQWry.Dat�е�ƫ�Ƽ�¼����3�ֽڣ�������ȡ��3�ֽڵ�ƫ�����ĳ����ʾ
        QQWry.Datʹ�á��ַ������洢��Щֵ'''
        s = self.img[offset: offset + 3]
        s += '\0'
        # unpack��һ��'I'��Ϊformat��������ַ���������4�ֽ�
        return unpack('I', s)[0]

    def getAreaAddr(self, offset = 0):
        ''' ͨ������ƫ��ֵ��ȡ��������Ϣ�ַ�����'''
        
        byte = ord(self.img[offset])
        if byte == 1 or byte == 2:
            # ��һ���ֽ�Ϊ1����2ʱ��ȡ��2-4�ֽ���Ϊһ��ƫ���������Լ�
            p = self.getLong3(offset + 1)
            return self.getAreaAddr(p)
        else:
            return self.getString(offset)

    def getAddr(self, offset, ip = 0):
        img = self.img
        o = offset
        byte = ord(img[o])

        if byte == 1:
            # �ض���ģʽ1
            # [IP][0x01][���Һ͵�����Ϣ�ľ���ƫ�Ƶ�ַ]
            # ʹ�ý�������3�ֽ���Ϊƫ���������ֽ�ȡ����Ϣ
            return self.getAddr(self.getLong3(o + 1))
		
        if byte == 2:
            # �ض���ģʽ2
            # [IP][0x02][������Ϣ�ľ���ƫ��][������Ϣ�ַ���]
            # ʹ�ù�����Ϣƫ���������Լ�ȡ���ַ�����Ϣ
            cArea = self.getAreaAddr(self.getLong3(o + 1))
            o += 4
            # ����ǰ4�ֽ�ȡ�ַ�����Ϊ������Ϣ
            aArea = self.getAreaAddr(o)
            return (cArea, aArea)
			
        if byte != 1 and byte != 2:
            # ��򵥵�IP��¼��ʽ��[IP][������Ϣ][������Ϣ]
            # �ض���ģʽ1�����������ƫ����ָ��������Һ͵�����Ϣ�����ַ���
            # ��ƫ����ָ��ĵ�һ���ֽڲ���1��2,��ʹ������ķ�֧
            # �򵥵�˵��ȡ����ȡ�����ַ�����
            cArea = self.getString(o)
            o += len(cArea) + 1
            aArea = self.getString(o)
            return (cArea, aArea)

    def find(self, ip, l, r):
        ''' ʹ�ö��ַ����������ֽڱ����IP��ַ��������¼'''
        if r - l <= 1:
            return l

        m = (l + r) / 2
        o = self.firstIndex + m * 7
        new_ip = unpack('I', self.img[o: o+4])[0]
        if ip <= new_ip:
            return self.find(ip, l, m)
        else:
            return self.find(ip, m, r)
		
    def getIPAddr(self, ip):
        ''' ��������������ȡ����Ϣ��'''
        # ʹ�������ֽڱ���IP��ַ
        ip = unpack('!I', socket.inet_aton(ip))[0]
        # ʹ�� self.find ��������ip������ƫ��
        i = self.find(ip, 0, self.indexCount - 1)
        # �õ�������¼
        o = self.firstIndex + i * 7
        # ������¼��ʽ�ǣ� ǰ4�ֽ�IP��Ϣ+3�ֽ�ָ��IP��¼��Ϣ��ƫ����
        # �������ʹ�ú�3�ֽ���Ϊƫ�����õ��䳣���ʾ��QQWry.Dat���ַ�����ʾֵ��
        o2 = self.getLong3(o + 4)
        # IP��¼ƫ��ֵ+4���Զ���ǰ4�ֽڵ�IP��ַ��Ϣ��
        (c, a) = self.getAddr(o2 + 4)
        return (c, a)
		
    def output(self, first, last):
        for i in range(first, last):
            o = self.firstIndex +  i * 7
            ip = socket.inet_ntoa(pack('!I', unpack('I', self.img[o:o+4])[0]))
            offset = self.getLong3(o + 4)
            (c, a) = self.getAddr(offset + 4)
            print "%s %d %s/%s" % (ip, offset, c, a)


def main():
    i = IPInfo('QQWry.Dat')
    (c, a) = i.getIPAddr(sys.argv[1])
    print '%s %s/%s' % (sys.argv[1], c, a)

if __name__ == '__main__':
    main()
