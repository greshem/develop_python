#!/usr/bin/python
#coding:gbk
import time,datetime                       #���ȵ�������ʹ�õ���ģ��
string = '2009-12-09'
string = time.strptime(string,'%Y-%m-%d') #���Ȱ��ַ���ʹ��strptime()����һ��ʱ��Ԫ�ع��ɵ�Ԫ��
print string;
string[0:3]                      #�ѵõ���ʱ��Ԫ��ǰ����Ԫ�ظ�ֵ����������(Ҳ����������)
#string = datetime.datetime(y, m, d)        #���ʹ��datetime�Ѹղŵõ���ʱ�����תΪ��ʽ��ʱ���ʽ����
												#2009-12-09 00:00:00                            #����,����˵������ַ�����ʱ���ת��(ע���Ǳ�������ת���Ĺ���)  <></></> </>
