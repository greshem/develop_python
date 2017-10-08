#coding=utf-8
import jieba
import jieba.posseg as pseg
import time
import  codecs;
import sys;
reload(sys);
sys.setdefaultencoding("utf-8");

if __name__ == '__main__':
    
    t1=time.time()
    output = codecs.open('output.txt','a+','utf-8')

    count=0;
    for each in  open("/root/wiki_chs00.txt","r"):
        if each.startswith("<doc")  or  each.startswith("</doc>"):
            continue;
        count+=1;
        if count%1000==0:
            print count;
        #print each; 
        words = jieba.cut(each) #进行分词
        #print " ".join(words);
        line= " ".join(words);
        output.write( line );

    output.close()
    print("分词及词性标注完成，耗时："+str(t2-t1)+"秒。") #反馈结果
