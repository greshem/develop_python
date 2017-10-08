#! /usr/bin/python   
# -*- coding: utf-8 -*-   
import urllib,re,unicodedata,string,sys   
from time import strftime,localtime   
channel={"1":"CCTV-1","2":"CCTV-2","3":"CCTV-3","4":"CCTV-4����",   
        "5":"CCTV-4ŷ��","6":"CCTV-4����","7":"CCTV-5","8":"CCTV-6",   
        "9":"CCTV-7","10":"CCTV-8","11":"CCTV-9","12":"CCTV-10",   
        "13":"CCTV-11","14":"CCTV-12","15":"CCTV����","16":"CCTV�ٶ�",   
        "17":"CCTV����","18":"CCTV_E","19":"CCTV-F","20":"CCTV-����"}   
if __name__=="__main__":   
        print "@@"  
        print "@@ ������������к���������(1-20)��ѡ��Ƶ�� "  
        print "@@ ͨ���������к����help��ȡƵ���б�"  
        print "@@"  
        if len(sys.argv)==1:   
                Select="8"  
        else:   
                if sys.argv[1]=="help":   
                        for i in range(len(channel)):   
                                print "%3d : %11s" % (i+1, channel["%s" % (i+1)]),   
                                if(i%4 == 3):   
                                        print ""   
                        sys.exit(0)   
                if string.atoi(sys.argv[1])>20 or string.atoi(sys.argv[1])<=0:   
                        print "Out of Range. Please Select 1-20."  
                        sys.exit(0)   
                else:   
                        Select=sys.argv[1]   
        print '���ڻ�ȡ��Ŀ�������Ժ�...'  
        date=strftime('%Y%m%d',localtime())   
        response = urllib.urlopen("http://tv.cctv.com/soushi/28/0"+Select+"/"+date+".shtml")   
        Result=response.read()   
        #list=re.findall(r"<div class='tlb_right'><div class='l'>(.+?)<script",Result,re.S)   
        list=re.findall(r"�����Ŀ(.+?)<script",Result,re.S)   
        list2=re.findall(r"<li>(.+?)</li>",list[0],re.S)   
        morning=[]   
        afternoon=[]   
        listnum=0  
        for i in range(len(list2)):   
                i=re.sub('<.+?>','',list2[i])   
                if string.atoi(i[:2])>=12:  #������Ľ�Ŀ������Ľ�Ŀ�ֿ�   
                        afternoon.append(i)   
                else:   
                        morning.append(i)   
        if len(morning)>len(afternoon):   
                listnum=len(morning)   
        else:   
                listnum=len(afternoon)   
        print "-"*80,   
        print " "*13+"�����Ŀ"+" "*26+"�����Ŀ"  
        print " "*14+"========"+" "*26+"========"  
        for i in range(listnum):   
                if(i<len(morning)):   
                        print "%-4s %-29s" %(morning[i][:5],morning[i][5:]),   
                else:   
                        print " "*35,   
                if(i<len(afternoon)):   
                        print "%-4s %-30s" %(afternoon[i][:5],afternoon[i][5:])   
                else:   
                        print " "*37  
        print "-"*80,   
        print " "*24,strftime("%Y��%m��%d��"),   
        print "%s ��Ŀ��" %channel[Select] 
