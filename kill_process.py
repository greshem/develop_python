#coding:gbk
#Python语言: windows平台下如何用Python杀进程
#from : http://www.joyloft.net/?p=1031
# "这段代码来自于一个很简单的场景：
#  在python中调一个程序。给这个程序设置一个timeout
#  假如一段时间程序还没有返回，就杀掉这个这个新开的进程。
#  本来以为我肯定不是第一个遇到这个问题的人，
#  但是网上搜了好久都没找到完整的办法，自己搞了一个。"

import ctypes
import sys

TH32CS_SNAPPROCESS = 0x00000002
class PROCESSENTRY32(ctypes.Structure):
     _fields_ = [("dwSize", ctypes.c_ulong),
                 ("cntUsage", ctypes.c_ulong),
                 ("th32ProcessID", ctypes.c_ulong),
                 ("th32DefaultHeapID", ctypes.c_ulong),
                 ("th32ModuleID", ctypes.c_ulong),
                 ("cntThreads", ctypes.c_ulong),
                 ("th32ParentProcessID", ctypes.c_ulong),
                 ("pcPriClassBase", ctypes.c_ulong),
                 ("dwFlags", ctypes.c_ulong),
                 ("szExeFile", ctypes.c_char * 260)]

def getProcList():
    CreateToolhelp32Snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot
    Process32First = ctypes.windll.kernel32.Process32First
    Process32Next = ctypes.windll.kernel32.Process32Next
    CloseHandle = ctypes.windll.kernel32.CloseHandle
    hProcessSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
    pe32 = PROCESSENTRY32()
    pe32.dwSize = ctypes.sizeof(PROCESSENTRY32)
    if Process32First(hProcessSnap,ctypes.byref(pe32)) == False:
        print >> sys.stderr, "Failed getting first process."
        return
    while True:
        yield pe32
        if Process32Next(hProcessSnap,ctypes.byref(pe32)) == False:
            break
    CloseHandle(hProcessSnap)

def getChildPid(pid):
    procList = getProcList()
    for proc in procList:
        if proc.th32ParentProcessID == pid:
            yield proc.th32ProcessID
    
def killPid(pid):
    childList = getChildPid(pid)
    for childPid in childList:
        killPid(childPid)
    handle = ctypes.windll.kernel32.OpenProcess(1, False, pid)
    ctypes.windll.kernel32.TerminateProcess(handle,0)


if __name__ =='__main__':
    args = sys.argv 
    if len(args) >1 :
        pid = int(args[1])
        killPid(pid)
    else:
        procList = getProcList()
        for proc in procList:
            print proc.szExeFile+'  '+str(proc.th32ParentProcessID) + '  '+str(proc.th32ProcessID)
    

#----------------------
#
# Usage demo
#
#----------------------
import subprocess
import time

import winproc

timeout = 2
process = subprocess.Popen("cmd /k ping localhost -t",shell = True)
start = int(time.time())
while process.poll()==None:
    now = int(time.time())
    if int (now - start) >timeout:
        pid = process.pid
        break

winproc.killPid(pid)
        
print "End"

