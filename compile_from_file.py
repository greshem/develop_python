#!/usr/bin/python
#coding:gbk
import os
import sys
import re
import copy

global g_cur_dir
g_cur_dir=''

#包含解析文件得到的属性数据,数据信息主要包括是哪种平台,以及是否需要gtest,cppunit,mysql,wx等的支持
class App_type:
	def __init__(self):
		self.frame_app={"wxwidgets_app":0,
			"mfc_app":0,
			"win_sdk_app":0,
			"console_app":0,
			"cppunit_support":0,
			"gtest_support":0,
			"mysql_support":0,
			"wx_support":0}

	def Add(self,type):
		self.frame_app[type]=self.frame_app[type]+1
	def Get(self):
		return self.frame_app;
	def __repr__(self):
		return "%s"%self.frame_app;

########################################################################
########################################################################
########################################################################
#一个目录下解析每个文件，自己提取项目构建需要的特征. 
class Project_build_traits:
	m_cppfile_traits_db={}
	########################################################################
	#检查是否是普通应用程序,匹配程序中的main函数,但对于注释行中的main则不予匹配
	def _match_console_app(self,line):
		main_c_comment = re.compile(r'.*/\*.*main\s*\(')
		main_cplus_comment = re.compile(r'.*//.*main\s*\(')
		main = re.compile(r'\s*main\s*\(')
		if main.search(line) and not main_cplus_comment.search(line) and not main_c_comment.search(line):
			return 1;
		return 0

	########################################################################
	#检查是否是wx的gui应用程序,匹配程序中的IMPLEMENT_APP函数,但对于注释行中的IMPLEMENT_APP则不予匹配
	def _match_wxwidgets_app(self,line):
		wx = re.compile(r'\s*IMPLEMENT_APP\s*\(')
		wx_c_comment = re.compile(r'.*/\*.*IMPLEMENT_APP\s*\(')
		wx_cplus_comment = re.compile(r'.*//.*IMPLEMENT_APP\s*\(')
		if wx.search(line) and not wx_c_comment.search(line) and not wx_cplus_comment.search(line):
			return 1
		return 0
	
	########################################################################
	#检查是否是mfc的gui应用程序,匹配程序中的BEGIN_MESSAGE_MAP函数等,但对于注释行中的BEGIN_MESSAGE_MAP等则不予匹配
	def _match_mfc_app(self,line):
		mfc = re.compile(r'^\s*BEGIN_MESSAGE_MAP\s*\(.*,\s*CWinApp\)')
		mfc_c_comment = re.compile(r'.*/\*.*BEGIN_MESSAGE_MAP\s*\(.*,\s*CWinApp\)')
		mfc_cplus_comment = re.compile(r'.*//.*BEGIN_MESSAGE_MAP\s*\(.*,\s*CWinApp\)')
		if mfc.search(line) and not mfc_c_comment.search(line) and not mfc_cplus_comment.search(line):
			return 1;
		return 0
			
#	def check_sdk_main(self,line,path,str):
#		sdk = re.compile(r'winmain\s*\(')
#		if sdk.search(line):
#			if "main"==plat or "mfc"==plat or "wx"==plat:
#				print "错误，sdk和其它的程序一起出现了"
#				sys.exit()
#			if "sdk"==plat:
#				continue
#			else:
#				plat="sdk"

	########################################################################
	#对于注释行中的出现的字段则不予匹配
	def _match_cppunit(self,line):
		cppunit = re.compile(r'^\s*#\s*include\s*.*cppunit\/')
		cppunit_c_comment = re.compile(r'.*/\*.*#\s*include\s*.*cppunit\/')
		cppunit_cplus_comment = re.compile(r'.*//.*#\s*include\s*.*cppunit\/')
		if cppunit.search(line) and not cppunit_c_comment.search(line) and not cppunit_cplus_comment.search(line):
			return 1
		return 0
	
	########################################################################
	#对于注释行中的出现的字段则不予匹配
	def _match_wx(self,line):
		wx = re.compile(r'^\s*#\s*include\s*.*wx/.*\.h')
		wx_c_comment = re.compile(r'.*/\*.*#\s*include\s*.*wx/.*\.h')
		wx_cplus_comment = re.compile(r'.*//.*#\s*include\s*.*wx/.*\.h')
		if wx.search(line) and not wx_c_comment.search(line) and not wx_cplus_comment.search(line):
			return 1
		return 0
	
	########################################################################
	#对于注释行中的出现的字段则不予匹配
	def _match_mysql(self,line):
		mysql = re.compile(r'^\s*#\s*include\s*.*mysql\.')
		mysql_c_comment = re.compile(r'.*/\*.*#\s*include\s*.*mysql\.')
		mysql_cplus_comment = re.compile(r'.*//.*s#\s*include\s*.*mysql\.')
		if mysql.search(line) and not mysql_c_comment.search(line) and not mysql_cplus_comment.search(line):
			return 1
		return 0
	
	########################################################################
	#对于注释行中的出现的字段则不予匹配
	def _match_gtest(self,line):
		gtest = re.compile(r'^\s*#\s*include\s*<gtest\/')
		gtest_c_comment = re.compile(r'.*/\*.*#\s*include\s*<gtest\/')
		gtest_cplus_comment = re.compile(r'.*//.*#\s*include\s*<gtest\/')
		if gtest.search(line) and not gtest_c_comment.search(line) and not gtest_cplus_comment.search(line):
			return 1
		return 0
	
	########################################################################
	#解析每个文件，进行平台和是否需要gtest,cppunit,mysql,wx等的支持判断
	def _get_file_traits(self,file):
		app_type=App_type();

		f = open(file,"rb")
		while True:
			line = f.readline()
			if len(line) == 0: # Zero length indicates EOF
				f.close()
				break
			if self._match_console_app(line):
				app_type.Add("console_app");
			if self._match_wxwidgets_app(line):
				app_type.Add("wxwidgets_app");
			if self._match_mfc_app(line):
				app_type.Add("mfc_app");
			if self._match_cppunit(line):
				app_type.Add("cppunit_support")
			if self._match_wx(line):
				app_type.Add("wx_support")
			if self._match_mysql(line):
				app_type.Add("mysql_support")
			if self._match_gtest(line):
				app_type.Add("gtest_support")
				#check_sdk_main(self,line,file,data_str)
		#返回字典,而不是类
		return app_type.Get();

	########################################################################
	#获取这个目录下的所有的.CPP,.C,.CC,.HPP等文件的要验证处理的特性 
	def get_dir_traits(self):
		for each_file in os.listdir(g_cur_dir):
			if is_cpp_file(each_file) or is_header_file(each_file):
				#创建一个字典,这里已经是Matrix了,所以后面解析这个Matrix的时候,就需要2次历遍
				self.m_cppfile_traits_db[each_file]=self._get_file_traits(each_file)
			else:
				print each_file,"不是cppfile";
		
		return self.m_cppfile_traits_db;
			
########################################################################
########################################################################
########################################################################
#创建build.bkl文件
class Create_bakefile:
	#通用的bakefile处理
	str_common='''	<cxxflags>/DWIN32</cxxflags>
			<cxxflags>/D_DEBUG</cxxflags>			
			<cxxflags>/D_WINDOWS</cxxflags>
			<cxxflags>/DNOPCH</cxxflags>
			<cxxflags>/DWINDOWSCODE</cxxflags>
			<cxxflags>/MTd</cxxflags>
			<include>D:\usr\include</include>
			<lib-path>D:\usr\lib</lib-path>
			<sys-lib>winmm</sys-lib>
			<sys-lib>comctl32</sys-lib>
			<sys-lib>rpcrt4</sys-lib>
			<sys-lib>wsock32</sys-lib>
			<sys-lib>odbc32</sys-lib>
			<sys-lib>kernel32</sys-lib>
			<sys-lib>user32</sys-lib>
			<sys-lib>gdi32</sys-lib>
			<sys-lib>winspool</sys-lib>
			<sys-lib>comdlg32</sys-lib>
			<sys-lib>advapi32</sys-lib>
			<sys-lib>shell32</sys-lib>
			<sys-lib>ole32</sys-lib>
			<sys-lib>oleaut32</sys-lib>
			<sys-lib>uuid</sys-lib>
			<sys-lib>odbccp32</sys-lib>
			<sys-lib>ws2_32</sys-lib>
			'''
	#注意d:\\usr\\lib 是用  /root/netware_emulator/management_UI/netware_emu_dev_env_setup.py 设置的 	
	str_wx='''<define>wxUSE_OLE</define>
			<define>WXUSINGDLL</define>
			<cxxflags>/D_UNICODE</cxxflags>
			<cxxflags>/D__WXMSW__</cxxflags>
			<cxxflags>/D__WXDEBUG__</cxxflags>
			<include>D:\usr\include\msvc</include>
			<sys-lib>wxmsw28ud_core</sys-lib>
			<sys-lib>wxbase28ud_net</sys-lib>
			<sys-lib>wxbase28ud</sys-lib>
			<sys-lib>wxtiffd</sys-lib>
			<sys-lib>wxjpegd</sys-lib>
			<sys-lib>wxpngd</sys-lib>
			<sys-lib>wxzlibd</sys-lib>
			<sys-lib>wxregexud</sys-lib>
			<sys-lib>wxexpatd</sys-lib>
			'''
	
	#mfc , 注意里面的宏.
	str_mfc='''<cxxflags>/D_AFXDLL</cxxflags> 
			<cxxflags>/D_MBCS</cxxflags>
			<cxxflags>/MDd</cxxflags>
			<ldflags>/INCREMENTAL:NO</ldflags>
			<ldflags>/NOLOGO</ldflags>
			<ldflags>/NODEFAULTLIB:LIBCMTD.lib</ldflags>
			<ldflags>/DEBUG</ldflags>
			<ldflags>/SUBSYSTEM:WINDOWS</ldflags>
			<ldflags>/MACHINE:X86</ldflags>
			'''
	str_gtest='''<sys-lib>gtest</sys-lib>
			'''
	str_cppunit='''<ldflags>/NODEFAULTLIB:libcmt.lib</ldflags>
			<sys-lib>cppunitd</sys-lib>
		'''
	str_mysql='''<include>D:\usr\include\lmyunit</include>
		<sys-lib>mysqlclient</sys-lib>
		'''
	#存放当前目录中所有含有main的.cpp,.cc,.c等文件名的集合
	main_file_array=[]
	#存放当前目录中所有不含main的.cpp,.cc,.c等文件名的集合
	nomain_file_array=[]
	#字典,用于处理wx和mfc的<include file="presets/wx.bkl"/>等
	dict_tag_include={
					"wx":'''<include file="presets/wx.bkl"/>
		''',
					"mfc":""
					}
	bkl_tag_makefile_starts='''<?xml version="1.0" ?>
	<!-- $Id: bakefile_quickstart.txt,v 1.5 2006/02/11 18:41:11 KO Exp $ -->
	
	
<makefile>
	'''
	#要写进build.bkl文件的bakefile_str数据
	bakefile_str=bkl_tag_makefile_starts
	#值取自字典dict_tag_include中的数据
	bkl_tag_include=''
	bakefile_makefile_tag_end='''
</makefile>'''
	#判断是main平台还是lib,值为0表示lib
	app_or_lib=0
	#对.rc资源文件的支持
	str_res=''
	#存放当前目录中所有.rc等文件名的集合
	rc_file_array=[]
	
	########################################################################
	#对当前目录下每一个.cpp,.c,.cc,.hpp等文件属性进行判断,对一个文件中出现多个main的情况,直接退出;
	#否则判断是App应用程序,还是Lib库
	def find_file_traits(self,file_array):
		for each_file,value in file_array.items():
			if value.get("wxwidgets_app")>1:
				print "错误，"+each_file+"文件中出现wx的main多个"
				sys.exit()
			elif value.get("mfc_app")>1:
				print "错误，"+each_file+"文件中出现mfc的main多个"
				sys.exit()
			elif value.get("win_sdk_app")>1:
				print "错误，"+each_file+"文件中出现sdk的main多个"
				sys.exit()
			elif value.get("console_app")>1:
				print "错误，"+each_file+"文件中出现posix的main多个"
				sys.exit()
			elif value.get("console_app")+value.get("wxwidgets_app")+value.get("mfc_app")+value.get("win_sdk_app")>1:
				print "错误，"+each_file+"文件中出现posix,wx,mfc,sdk中的两个或多个"
				sys.exit()
			elif value.get("console_app")==1 or value.get("wxwidgets_app")==1 or value.get("mfc_app")==1 or value.get("win_sdk_app")==1:
				print "App类型"
				self.app_or_lib=1
	
	########################################################################
	#给main_file_array数组赋值
	def assign_main_file_array(self,file_array):
		for each_file,value in file_array.items():
			if value.get("console_app")==1 or value.get("wxwidgets_app")==1 or value.get("mfc_app")==1 or value.get("win_sdk_app")==1:
				self.main_file_array.append(each_file)

	########################################################################
	#给rc_file_array数组赋值
	def assign_rc_file_array(self):
		for file in os.listdir(g_cur_dir):
			if is_rc_file(file):
				self.rc_file_array.append(file)

	########################################################################
	#给nomain_file_array数组赋值
	def assign_nomain_file_array(self):
		for file in os.listdir(g_cur_dir):
			if is_cpp_file(file) and not file in self.main_file_array:
				self.nomain_file_array.append(file)
				
	########################################################################
	#如果有资源文件,则添加对它的处理
	def gen_str_res(self):
		self.str_res=''
		for each_file in self.rc_file_array:
			if each_file.endswith(".rc"):
				self.str_res=self.str_res+'''<win32-res>'''+each_file+'''</win32-res>
			'''		
	
	def gen_str_include_tag(self,file_traits_array):
		mfc=0
		wx=0
		for each_file,values in file_traits_array.items():
			if values.get("mfc_app")==1:
				if mfc==0:
					mfc=1
					self.bkl_tag_include=self.dict_tag_include.get("mfc")
					self.bakefile_str=self.bakefile_str+self.bkl_tag_include
			if values.get("wx_support")>0:
				if wx==0:
					wx=1
					self.bkl_tag_include=self.dict_tag_include.get("wx")
					self.bakefile_str=self.bakefile_str+self.bkl_tag_include
	
	########################################################################
	#开始创建bakefile_str的第二层循环,第一层循环在create_bkl_file中
	#检查是否需要gtest,cppunit,mysql,wx,mfc,资源文件等的支持
	def gen_str_include_lib(self,file_array,file):
		gtest=0
		cppunit=0
		mysql=0
		wx=0
		mfc=0
		#添加通用的bakefile处理
		self.bakefile_str=self.bakefile_str+self.str_common
		for each_file,value in file_array.items():
			#处理当前含有main的文件或者不含有main的文件
			if each_file==file or each_file not in self.main_file_array:
				if value.get("gtest_support")>0:
					if gtest==0:
						gtest=1
						self.bakefile_str=self.bakefile_str+self.str_gtest
				if value.get("cppunit_support")>0:
					if cppunit==0:
						cppunit=1
						self.bakefile_str=self.bakefile_str+self.str_cppunit
				if value.get("mysql_support")>0:
					if mysql==0:
						mysql=1
						self.bakefile_str=self.bakefile_str+self.str_mysql
				if value.get("wx_support")>0:
					if wx==0:
						wx=1
						self.bakefile_str=self.bakefile_str+self.str_wx
				if value.get("mfc_app")==1:
					if mfc==0:
						mfc=1
						self.bakefile_str=self.bakefile_str+self.str_mfc
		#添加对资源文件的处理
		self.gen_str_res()
		self.bakefile_str=self.bakefile_str+self.str_res
	
	########################################################################
	#处理当前目录下含有main的一个文件
	#是普通控制台应用程序,生成的exe文件名来自当前处理的文件名
	#编译的对象文件为当前处理的文件和其它不含有main的所有.cpp,.c,.cc,.hpp等文件
	def gen_str_exe_console_app(self,file_traits_array,file):
		self.bakefile_str=self.bakefile_str+'''	
		<exe id="'''
		#(file.split('.'))[0]为解析得到.cpp,.c,.cc,.hpp等文件的前缀
		#如file=dictTest.cpp,经过(file.split('.'))[0],得到的是dictTest
		self.bakefile_str=self.bakefile_str+(file.split('.'))[0]+'''">
			<app-type>console</app-type>
		'''
		
		#添加gtest,cppunit,mysql,wx,mfc,资源文件等的支持
		self.gen_str_include_lib(file_traits_array,file)
		
		#编译对象是当前目录下其它不含有main的所有.cpp,.c,.cc,.hpp等文件
		for each_file in self.nomain_file_array:
			self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+each_file+'''"))</sources>
			'''
		#编译对象是当前处理的文件
		self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+file+'''"))</sources>
		'''
		self.bakefile_str=self.bakefile_str+'''</exe>
					'''

	########################################################################
	#处理当前目录下含有main的一个文件
	#是wx的应用程序,生成的exe文件名来自当前处理的文件名
	#编译的对象文件为当前处理的文件和其它不含有main的所有.cpp,.c,.cc,.hpp等文件
	def gen_str_wx_exe_gui_tag(self,file_traits_array,file):
		self.bakefile_str=self.bakefile_str+'''
		<exe id="'''
		#(file.split('.'))[0]为解析得到.cpp,.c,.cc,.hpp等文件的前缀
		#如file=dictTest.cpp,经过(file.split('.'))[0],得到的是dictTest
		self.bakefile_str=self.bakefile_str+(file.split('.'))[0]+'''">
			<app-type>gui</app-type>
		'''
		
		#添加gtest,cppunit,mysql,wx,mfc,资源文件等的支持
		self.gen_str_include_lib(file_traits_array,file)
		
		#编译对象是当前目录下其它不含有main的所有.cpp,.c,.cc等文件
		for each_file in self.nomain_file_array:
			self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+each_file+'''"))</sources>
			'''
		#编译对象是当前处理的文件
		self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+file+'''"))</sources>
		'''
		self.bakefile_str=self.bakefile_str+'''</exe>
		'''

	########################################################################
	#处理当前目录下含有main的一个文件
	#是mfc的应用程序,生成的exe文件名来自当前处理的文件名
	#编译的对象文件为当前处理的文件和其它不含有main的所有.cpp,.c,.cc,.hpp等文件
	def gen_str_mfc_app_exe_tag(self,file_traits_array,file):
		self.bakefile_str=self.bakefile_str+'''	
		<exe id="'''
		#(file.split('.'))[0]为解析得到.cpp,.c,.cc,.hpp等文件的前缀
		#如file=dictTest.cpp,经过(file.split('.'))[0],得到的是dictTest
		self.bakefile_str=self.bakefile_str+(file.split('.'))[0]+'''">
			<app-type>gui</app-type>
		'''
		
		#添加gtest,cppunit,mysql,wx,mfc,资源文件等的支持
		self.gen_str_include_lib(file_traits_array,file)
		
		#编译对象是当前目录下其它不含有main的所有.cpp,.c,.cc等文件
		for each_file in self.nomain_file_array:
			self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+each_file+'''"))</sources>
			'''

		#编译对象是当前处理的文件
		self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+file+'''"))</sources>
		'''
		self.bakefile_str=self.bakefile_str+'''</exe>
		'''

	########################################################################
	#编译生成动态库,生成库的文件名来自当前目录名
	def str_create_lib_tag(self,file_traits_array,file):
		self.bakefile_str=self.bakefile_str+'''
		<lib id="'''
		#app_name为当前目录用分隔符'\'分割后,得到的数组
		app_name=g_cur_dir.split(os.sep)
		self.bakefile_str=self.bakefile_str+app_name[len(app_name)-1]+'''">
		'''
		
		#添加gtest,cppunit,mysql,wx,mfc,资源文件等的支持
		self.gen_str_include_lib(file_traits_array,file)
		
		#编译对象是当前目录下所有.cpp,.c,.cc,.hpp等文件
		for each_file in self.nomain_file_array:
			self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+each_file+'''"))</sources>
		'''
		self.bakefile_str=self.bakefile_str+'''</lib>
'''
	
	########################################################################
	#在当前目录生成bakefile文件
	#判断文件属性类型,是App应用程序则开始创建bakefile_str的第一层循环
	#循环对当前目录下的所有含有main的文件进行挨个处理,否则生成一个动态库
	def create_bkl_file(self,file_traits_array):
		#判断文件属性
		self.find_file_traits(file_traits_array)
		
		self.assign_main_file_array(file_traits_array)
		self.assign_nomain_file_array()
		self.assign_rc_file_array()
		self.gen_str_include_tag(file_traits_array)
		#是App应用程序,检测是哪种类型的应用程序,并作对应的处理
		if 1==self.app_or_lib:
			for each_file,values in file_traits_array.items():
				if values.get("console_app")==1:
					print "***********posix_main************"
					self.gen_str_exe_console_app(file_traits_array,each_file)
				elif values.get("wxwidgets_app")==1:
					print "***********wx_main************"
					self.gen_str_wx_exe_gui_tag(file_traits_array,each_file)
				elif values.get("mfc_app")==1:
					print "***********mfc_main************"
					self.gen_str_mfc_app_exe_tag(file_traits_array,each_file)
				#elif values.get("win_sdk_app")==1:
				#	print "***********win_sdk_main************"
				#	self.str_create_sdk_main()
		#是Lib库,生成动态库
		else:
			print "***********lib************"
			file=''
			self.str_create_lib_tag(file_traits_array,file)
		self.bakefile_str=self.bakefile_str+self.bakefile_makefile_tag_end
		
		f=open("build.bkl","wt")
		f.write(self.bakefile_str)
		f.close()

########################################################################
def is_cpp_file(file):
	if file.endswith(".cpp") or file.endswith(".c") or file.endswith(".cc"):
		return 1
	return 0

def is_header_file(file):
	if file.endswith(".h") or file.endswith(".hpp") or  file.endswith(".hh") or file.endswith(".hxx"):
		return 1
	return 0
	
########################################################################
def is_rc_file(file):
	if file.endswith(".rc"):
		return 1
	return 0
	
########################################################################
if __name__ == "__main__":
	if "clean"==sys.argv[len(sys.argv)-1]:
		if os.path.exists("build.bkl"):
			os.system("del build.bkl")
		if os.path.exists("makefile.vc"):
			os.system("nmake /f makefile.vc clean")
			os.system("del makefile.vc")
	else:
		g_cur_dir=os.getcwd()
		
		build_traits=Project_build_traits()
		file_traits_array=build_traits.get_dir_traits()

		create_class=Create_bakefile()
		create_class.create_bkl_file(file_traits_array)

		if 0!=os.system("bakefile -f msvc build.bkl"):
			print "bakefile -f msvc build.bkl #failed, please check"
			sys.exit(1)
		if 0!=os.system("nmake /f makefile.vc"):
			print "nmake /f makefile.vc #failed, please check"
			sys.exit(2)
			
