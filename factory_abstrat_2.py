#coding:gbk

class CClientWindow(object):  
    """客户端窗口，代表客户端"""  
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
    """抽象菜单"""  
    def ShowMenu(self):  
        pass  
  
class CWindowsMenu(CMenu):  
    """具体菜单，用于Windows系统"""  
    def ShowMenu(self):  
        print 'CWindowsMenu ShowMenu'  
  
  
class CLinuxMenu(CMenu):  
    """具体菜单，用于Linux系统"""  
    def ShowMenu(self):  
        print 'CLinuxMenu ShowMenu'  
  
  
class CToolBar(object):  
    """抽象工具栏"""  
    def ShowToolBar(self):  
        pass  
  
  
class CWindowsToolBar(CToolBar):  
    """具体工具栏，用于Windows系统"""  
    def ShowToolBar(self):  
        print 'CWindowsToolBar ShowToolBar'  
  
  
class CLinuxToolBar(CToolBar):  
    """具体工具栏，用于Linux系统"""  
    def ShowToolBar(self):  
        print 'CLinuxToolBar ShowToolBar'  
  
class CCtrlFactory(object):  
    """抽象工厂，用于产生跨平台产生所有窗口控件"""  
    def GetMenu(self):  
        pass  
    def GetToolBar(self):  
        pass  
      
class CWindowsCtrlFactory(object):  
    """具体工厂，产生Windows下所需的所有窗口控件"""  
    def GetMenu(self):  
        return CWindowsMenu()  
    def GetToolBar(self):  
        return CWindowsToolBar()  
  
class CLinuxCtrlFactory(object):  
    """具体工厂，产生Linux下所需的所有窗口控件"""  
    def GetMenu(self):  
        return CLinuxMenu()  
    def GetToolBar(self):  
        return CLinuxToolBar()  
 
#客户程序运行  
wnd=CClientWindow(CWindowsCtrlFactory())  
wnd.ShowWindow()  

