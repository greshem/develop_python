# coding=gbk
'''
Created on 2011-1-7
@author: HH
'''
  
import os,ConfigParser

'''
�ݹ��г�ĳĿ¼�µ��ļ�������List��
'''
def listDir (fileList,path):
    files=os.listdir(path)
    for i in  files:
        file_path=path+"\\"+i
        if os.path.isfile(file_path):
            fileList.append(file_path)
    for i in files:
        file_path=path+"\\"+i
        if os.path.isdir(file_path):
            #fileList.append(file_path)
            listDir(fileList,file_path)
    return fileList

'''
��List������д���ļ�
'''
def writeListToFile(list,path):
    strs="\n".join(list)
    f=open(path,'wb')
    f.write(strs)
    f.close()

'''
�����ļ����ݲ�����List��
'''
def readFileToList(path):
    lists=[]
    f=open(path,'rb')
    lines=f.readlines()
    for line in lines:
        lists.append(line.strip())
    f.close()
    return lists

'''
�Ƚ��ļ�--��Set��ʽ
'''
def compList(list1,list2):
    return list(set(list1)-set(list2))

'''
����List���ļ���ָ��λ��
'''
def copyFiles(fileList,targetDir):
    for file in fileList:
        targetPath=os.path.join(targetDir,os.path.dirname(file))
        targetFile=os.path.join(targetDir,file)
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)
        if not os.path.exists(targetFile) or (os.path.exists(targetFile) and os.path.getsize(targetFile)!=os.path.getsize(file)):
            print "���ڸ����ļ���"+file
            open(targetFile,'wb').write(open(file,'rb').read())
        else:
            print "�ļ��Ѵ��ڣ������ƣ�"


if __name__ == '__main__':
    path=".svn"
    #��ȡԴĿ¼
    
    txtFile="1.txt"
    #Ŀ¼�ṹ�����Ŀ���ļ�
    
    tdir="cpfile"
    #���Ƶ���Ŀ��Ŀ¼
    
    cfFile="config.ini";
    #�����ļ��ļ���
    fileList=[]
    
    #��ȡ�����ļ�
    if(os.path.exists(cfFile)):
        cf=ConfigParser.ConfigParser()
        cf.read(cfFile)
        
        path=cf.get("main", "sourceDir")
        txtFile=cf.get("main","txtFile")
        tdir=cf.get("main","targetDir")
    else:
        print "�����ļ������ڣ�"
        raw_input("\n�� �س��� �˳�\n")
        exit()
    
    if(os.path.exists(txtFile)):
        #����������ļ����ڣ��Ͷ�ȡ��Ƚ�
        list1=readFileToList(txtFile)
        print "���ڶ�ȡ�ļ��б���"
        fileList=listDir (fileList,path)
        print "���ڱȽ��ļ�����"
        list_res=compList(fileList,list1)
        
        if len(list_res)>0:
            print "������ԭĿ¼�в����ڵ��ļ���\n"
            print "\n".join(list_res)
            print "\n�����ļ�����"+str(len(list_res))+"\n"
            if raw_input("\n�Ƿ����ļ�����y/n��")!='n':
                copyFiles(list_res,tdir)
        else:
            print "û�в���ͬ���ļ���"
    else:
        #����������ļ������ڣ��򵼳��ļ�
        print "���ڶ�ȡ�ļ��б���"
        fileList=listDir (fileList,path)
        writeListToFile(fileList,txtFile)
        print "�ѱ��浽�ļ���"+txtFile
        
    raw_input("\n�� �س��� �˳�\n")
