#coding:gbk

class CClientWindow(object):  
    """�ͻ��˴��ڣ�����ͻ���"""  
    def __init__(self,ctrlfactory):  
        self.SetCtrlFactory(ctrlfactory)  
          
    def SetCtrlFactory(self,ctrlfactory):  
        self.m_CtrlFactory=ctrlfactory  
        self.SetMenu(self.m_CtrlFactory.GetMenu())  
        self.SetToolBar(self.m_CtrlFactory.GetToolBar())  
          
    def SetMenu(self,menu):  
        self.m_Menu=menu  
          
    def SetToolBar(self,toolbar):  
        self.m_ToolBar=toolbar  
          
    def ShowWindow(self):  
        self.m_Menu.ShowMenu()  
        self.m_ToolBar.ShowToolBar()  
  
class CMenu(object):  
    """����˵�"""  
    def ShowMenu(self):  
        pass  
  
class CWindowsMenu(CMenu):  
    """����˵�������Windowsϵͳ"""  
    def ShowMenu(self):  
        print 'CWindowsMenu ShowMenu'  
  
  
class CLinuxMenu(CMenu):  
    """����˵�������Linuxϵͳ"""  
    def ShowMenu(self):  
        print 'CLinuxMenu ShowMenu'  
  
  
class CToolBar(object):  
    """���󹤾���"""  
    def ShowToolBar(self):  
        pass  
  
  
class CWindowsToolBar(CToolBar):  
    """���幤����������Windowsϵͳ"""  
    def ShowToolBar(self):  
        print 'CWindowsToolBar ShowToolBar'  
  
  
class CLinuxToolBar(CToolBar):  
    """���幤����������Linuxϵͳ"""  
    def ShowToolBar(self):  
        print 'CLinuxToolBar ShowToolBar'  
  
class CCtrlFactory(object):  
    """���󹤳������ڲ�����ƽ̨�������д��ڿؼ�"""  
    def GetMenu(self):  
        pass  
    def GetToolBar(self):  
        pass  
      
class CWindowsCtrlFactory(object):  
    """���幤��������Windows����������д��ڿؼ�"""  
    def GetMenu(self):  
        return CWindowsMenu()  
    def GetToolBar(self):  
        return CWindowsToolBar()  
  
class CLinuxCtrlFactory(object):  
    """���幤��������Linux����������д��ڿؼ�"""  
    def GetMenu(self):  
        return CLinuxMenu()  
    def GetToolBar(self):  
        return CLinuxToolBar()  
 
#�ͻ���������  
wnd=CClientWindow(CWindowsCtrlFactory())  
wnd.ShowWindow()  

