# # 
# Ϊ�˱���ض������ַ� # 
# �ļ�Ҫ���� unicode ���� # 
# txt�ļ����Ϊ�Ի��������������򣬿�ѡ�� # 
# �������ʽ # 
# # 
########################## 
import os 
import struct 
filename = str(raw_input("Please enter an old file name: ")) 
filenamepre = str(raw_input("Please enter an new file name prefix: ")) 
count = 0 
filecount = 0 
maxcount = 20 
newfilename = repr(filecount) + '.txt' 
oldfile = open(filename,'rb') 
bFirst = True 
while True: 
    s = oldfile.read(512*8 - 4) 
if not s: 
    exit() 
filecount = filecount + 1 
newfilename = filenamepre + repr(filecount).zfill(2) + '.txt' 
newfile = open(newfilename,'wb') 
if not bFirst: 
    be = 0XFEFF 
    newfile.write(struct.pack('H',be)) 
    newfile.write(s) 
be = 0X000A000D 
newfile.write(struct.pack('I',be)) 
newfile.close() 
bFirst = False 
oldfile.close() 
