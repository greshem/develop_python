#coding:gbk
import os  
import pythoncom  
from win32com.shell import shell  
from win32com.shell import shellcon 

#��.lnk�ļ��л�ȡ�ļ�·��

def GetpathFromLink(lnkpath):  
    shortcut = pythoncom.CoCreateInstance(  
        shell.CLSID_ShellLink, None,  
        pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)  
    shortcut.QueryInterface( pythoncom.IID_IPersistFile ).Load(lnkpath)  
    path = shortcut.GetPath(shell.SLGP_SHORTPATH)[0]  
    return path 

#������ݷ�ʽ
def CreateLnkpath(filename,lnkname):  
    shortcut = pythoncom.CoCreateInstance(  
        shell.CLSID_ShellLink, None,  
        pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)  
    shortcut.SetPath(filename)  
    if os.path.splitext(lnkname)[-1] != '.lnk':  
        lnkname += ".lnk"  
    shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(lnkname,0) 

#����url��ݷ�ʽ
def CreateURLShortcut(url,name):  
    shortcut = pythoncom.CoCreateInstance(  
        shell.CLSID_InternetShortcut,None,  
        pythoncom.CLSCTX_INPROC_SERVER,shell.IID_IUniformResourceLocator)  
    shortcut.SetURL(url)  
    if os.path.splitext(name)[-1] != '.url':  
        name += '.url'  
    shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(name,0) 

#��.url��ݷ�ʽ��ȡurl���ӵ�ַ
def GetURLFromShortcut(url):
 shortcut = pythoncom.CoCreateInstance(
     shell.CLSID_InternetShortcut,None,
     pythoncom.CLSCTX_INPROC_SERVER,shell.IID_IUniformResourceLocator)
 shortcut.QueryInterface(pythoncom.IID_IPersistFile).Load(url)
 url = shortcut.GetURL()
 return url
#��ȡ����·��

def GetDesktoppath():  
    ilist = shell.SHGetSpecialFolderLocation(0,shellcon.CSIDL_DESKTOP)  
    dtpath = shell.SHGetPathFromIDList(ilist)  
    #dtpath = dtpath.decode('gbk')  
    return dtpath 


if __name__ == '__main__':
	CreateLnkpath("c:\\", "C") 
