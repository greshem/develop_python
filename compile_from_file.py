#!/usr/bin/python
#coding:gbk
import os
import sys
import re
import copy

global g_cur_dir
g_cur_dir=''

#���������ļ��õ�����������,������Ϣ��Ҫ����������ƽ̨,�Լ��Ƿ���Ҫgtest,cppunit,mysql,wx�ȵ�֧��
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
#һ��Ŀ¼�½���ÿ���ļ����Լ���ȡ��Ŀ������Ҫ������. 
class Project_build_traits:
	m_cppfile_traits_db={}
	########################################################################
	#����Ƿ�����ͨӦ�ó���,ƥ������е�main����,������ע�����е�main����ƥ��
	def _match_console_app(self,line):
		main_c_comment = re.compile(r'.*/\*.*main\s*\(')
		main_cplus_comment = re.compile(r'.*//.*main\s*\(')
		main = re.compile(r'\s*main\s*\(')
		if main.search(line) and not main_cplus_comment.search(line) and not main_c_comment.search(line):
			return 1;
		return 0

	########################################################################
	#����Ƿ���wx��guiӦ�ó���,ƥ������е�IMPLEMENT_APP����,������ע�����е�IMPLEMENT_APP����ƥ��
	def _match_wxwidgets_app(self,line):
		wx = re.compile(r'\s*IMPLEMENT_APP\s*\(')
		wx_c_comment = re.compile(r'.*/\*.*IMPLEMENT_APP\s*\(')
		wx_cplus_comment = re.compile(r'.*//.*IMPLEMENT_APP\s*\(')
		if wx.search(line) and not wx_c_comment.search(line) and not wx_cplus_comment.search(line):
			return 1
		return 0
	
	########################################################################
	#����Ƿ���mfc��guiӦ�ó���,ƥ������е�BEGIN_MESSAGE_MAP������,������ע�����е�BEGIN_MESSAGE_MAP������ƥ��
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
#				print "����sdk�������ĳ���һ�������"
#				sys.exit()
#			if "sdk"==plat:
#				continue
#			else:
#				plat="sdk"

	########################################################################
	#����ע�����еĳ��ֵ��ֶ�����ƥ��
	def _match_cppunit(self,line):
		cppunit = re.compile(r'^\s*#\s*include\s*.*cppunit\/')
		cppunit_c_comment = re.compile(r'.*/\*.*#\s*include\s*.*cppunit\/')
		cppunit_cplus_comment = re.compile(r'.*//.*#\s*include\s*.*cppunit\/')
		if cppunit.search(line) and not cppunit_c_comment.search(line) and not cppunit_cplus_comment.search(line):
			return 1
		return 0
	
	########################################################################
	#����ע�����еĳ��ֵ��ֶ�����ƥ��
	def _match_wx(self,line):
		wx = re.compile(r'^\s*#\s*include\s*.*wx/.*\.h')
		wx_c_comment = re.compile(r'.*/\*.*#\s*include\s*.*wx/.*\.h')
		wx_cplus_comment = re.compile(r'.*//.*#\s*include\s*.*wx/.*\.h')
		if wx.search(line) and not wx_c_comment.search(line) and not wx_cplus_comment.search(line):
			return 1
		return 0
	
	########################################################################
	#����ע�����еĳ��ֵ��ֶ�����ƥ��
	def _match_mysql(self,line):
		mysql = re.compile(r'^\s*#\s*include\s*.*mysql\.')
		mysql_c_comment = re.compile(r'.*/\*.*#\s*include\s*.*mysql\.')
		mysql_cplus_comment = re.compile(r'.*//.*s#\s*include\s*.*mysql\.')
		if mysql.search(line) and not mysql_c_comment.search(line) and not mysql_cplus_comment.search(line):
			return 1
		return 0
	
	########################################################################
	#����ע�����еĳ��ֵ��ֶ�����ƥ��
	def _match_gtest(self,line):
		gtest = re.compile(r'^\s*#\s*include\s*<gtest\/')
		gtest_c_comment = re.compile(r'.*/\*.*#\s*include\s*<gtest\/')
		gtest_cplus_comment = re.compile(r'.*//.*#\s*include\s*<gtest\/')
		if gtest.search(line) and not gtest_c_comment.search(line) and not gtest_cplus_comment.search(line):
			return 1
		return 0
	
	########################################################################
	#����ÿ���ļ�������ƽ̨���Ƿ���Ҫgtest,cppunit,mysql,wx�ȵ�֧���ж�
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
		#�����ֵ�,��������
		return app_type.Get();

	########################################################################
	#��ȡ���Ŀ¼�µ����е�.CPP,.C,.CC,.HPP���ļ���Ҫ��֤��������� 
	def get_dir_traits(self):
		for each_file in os.listdir(g_cur_dir):
			if is_cpp_file(each_file) or is_header_file(each_file):
				#����һ���ֵ�,�����Ѿ���Matrix��,���Ժ���������Matrix��ʱ��,����Ҫ2������
				self.m_cppfile_traits_db[each_file]=self._get_file_traits(each_file)
			else:
				print each_file,"����cppfile";
		
		return self.m_cppfile_traits_db;
			
########################################################################
########################################################################
########################################################################
#����build.bkl�ļ�
class Create_bakefile:
	#ͨ�õ�bakefile����
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
	#ע��d:\\usr\\lib ����  /root/netware_emulator/management_UI/netware_emu_dev_env_setup.py ���õ� 	
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
	
	#mfc , ע������ĺ�.
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
	#��ŵ�ǰĿ¼�����к���main��.cpp,.cc,.c���ļ����ļ���
	main_file_array=[]
	#��ŵ�ǰĿ¼�����в���main��.cpp,.cc,.c���ļ����ļ���
	nomain_file_array=[]
	#�ֵ�,���ڴ���wx��mfc��<include file="presets/wx.bkl"/>��
	dict_tag_include={
					"wx":'''<include file="presets/wx.bkl"/>
		''',
					"mfc":""
					}
	bkl_tag_makefile_starts='''<?xml version="1.0" ?>
	<!-- $Id: bakefile_quickstart.txt,v 1.5 2006/02/11 18:41:11 KO Exp $ -->
	
	
<makefile>
	'''
	#Ҫд��build.bkl�ļ���bakefile_str����
	bakefile_str=bkl_tag_makefile_starts
	#ֵȡ���ֵ�dict_tag_include�е�����
	bkl_tag_include=''
	bakefile_makefile_tag_end='''
</makefile>'''
	#�ж���mainƽ̨����lib,ֵΪ0��ʾlib
	app_or_lib=0
	#��.rc��Դ�ļ���֧��
	str_res=''
	#��ŵ�ǰĿ¼������.rc���ļ����ļ���
	rc_file_array=[]
	
	########################################################################
	#�Ե�ǰĿ¼��ÿһ��.cpp,.c,.cc,.hpp���ļ����Խ����ж�,��һ���ļ��г��ֶ��main�����,ֱ���˳�;
	#�����ж���AppӦ�ó���,����Lib��
	def find_file_traits(self,file_array):
		for each_file,value in file_array.items():
			if value.get("wxwidgets_app")>1:
				print "����"+each_file+"�ļ��г���wx��main���"
				sys.exit()
			elif value.get("mfc_app")>1:
				print "����"+each_file+"�ļ��г���mfc��main���"
				sys.exit()
			elif value.get("win_sdk_app")>1:
				print "����"+each_file+"�ļ��г���sdk��main���"
				sys.exit()
			elif value.get("console_app")>1:
				print "����"+each_file+"�ļ��г���posix��main���"
				sys.exit()
			elif value.get("console_app")+value.get("wxwidgets_app")+value.get("mfc_app")+value.get("win_sdk_app")>1:
				print "����"+each_file+"�ļ��г���posix,wx,mfc,sdk�е���������"
				sys.exit()
			elif value.get("console_app")==1 or value.get("wxwidgets_app")==1 or value.get("mfc_app")==1 or value.get("win_sdk_app")==1:
				print "App����"
				self.app_or_lib=1
	
	########################################################################
	#��main_file_array���鸳ֵ
	def assign_main_file_array(self,file_array):
		for each_file,value in file_array.items():
			if value.get("console_app")==1 or value.get("wxwidgets_app")==1 or value.get("mfc_app")==1 or value.get("win_sdk_app")==1:
				self.main_file_array.append(each_file)

	########################################################################
	#��rc_file_array���鸳ֵ
	def assign_rc_file_array(self):
		for file in os.listdir(g_cur_dir):
			if is_rc_file(file):
				self.rc_file_array.append(file)

	########################################################################
	#��nomain_file_array���鸳ֵ
	def assign_nomain_file_array(self):
		for file in os.listdir(g_cur_dir):
			if is_cpp_file(file) and not file in self.main_file_array:
				self.nomain_file_array.append(file)
				
	########################################################################
	#�������Դ�ļ�,����Ӷ����Ĵ���
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
	#��ʼ����bakefile_str�ĵڶ���ѭ��,��һ��ѭ����create_bkl_file��
	#����Ƿ���Ҫgtest,cppunit,mysql,wx,mfc,��Դ�ļ��ȵ�֧��
	def gen_str_include_lib(self,file_array,file):
		gtest=0
		cppunit=0
		mysql=0
		wx=0
		mfc=0
		#���ͨ�õ�bakefile����
		self.bakefile_str=self.bakefile_str+self.str_common
		for each_file,value in file_array.items():
			#����ǰ����main���ļ����߲�����main���ļ�
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
		#��Ӷ���Դ�ļ��Ĵ���
		self.gen_str_res()
		self.bakefile_str=self.bakefile_str+self.str_res
	
	########################################################################
	#����ǰĿ¼�º���main��һ���ļ�
	#����ͨ����̨Ӧ�ó���,���ɵ�exe�ļ������Ե�ǰ������ļ���
	#����Ķ����ļ�Ϊ��ǰ������ļ�������������main������.cpp,.c,.cc,.hpp���ļ�
	def gen_str_exe_console_app(self,file_traits_array,file):
		self.bakefile_str=self.bakefile_str+'''	
		<exe id="'''
		#(file.split('.'))[0]Ϊ�����õ�.cpp,.c,.cc,.hpp���ļ���ǰ׺
		#��file=dictTest.cpp,����(file.split('.'))[0],�õ�����dictTest
		self.bakefile_str=self.bakefile_str+(file.split('.'))[0]+'''">
			<app-type>console</app-type>
		'''
		
		#���gtest,cppunit,mysql,wx,mfc,��Դ�ļ��ȵ�֧��
		self.gen_str_include_lib(file_traits_array,file)
		
		#��������ǵ�ǰĿ¼������������main������.cpp,.c,.cc,.hpp���ļ�
		for each_file in self.nomain_file_array:
			self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+each_file+'''"))</sources>
			'''
		#��������ǵ�ǰ������ļ�
		self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+file+'''"))</sources>
		'''
		self.bakefile_str=self.bakefile_str+'''</exe>
					'''

	########################################################################
	#����ǰĿ¼�º���main��һ���ļ�
	#��wx��Ӧ�ó���,���ɵ�exe�ļ������Ե�ǰ������ļ���
	#����Ķ����ļ�Ϊ��ǰ������ļ�������������main������.cpp,.c,.cc,.hpp���ļ�
	def gen_str_wx_exe_gui_tag(self,file_traits_array,file):
		self.bakefile_str=self.bakefile_str+'''
		<exe id="'''
		#(file.split('.'))[0]Ϊ�����õ�.cpp,.c,.cc,.hpp���ļ���ǰ׺
		#��file=dictTest.cpp,����(file.split('.'))[0],�õ�����dictTest
		self.bakefile_str=self.bakefile_str+(file.split('.'))[0]+'''">
			<app-type>gui</app-type>
		'''
		
		#���gtest,cppunit,mysql,wx,mfc,��Դ�ļ��ȵ�֧��
		self.gen_str_include_lib(file_traits_array,file)
		
		#��������ǵ�ǰĿ¼������������main������.cpp,.c,.cc���ļ�
		for each_file in self.nomain_file_array:
			self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+each_file+'''"))</sources>
			'''
		#��������ǵ�ǰ������ļ�
		self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+file+'''"))</sources>
		'''
		self.bakefile_str=self.bakefile_str+'''</exe>
		'''

	########################################################################
	#����ǰĿ¼�º���main��һ���ļ�
	#��mfc��Ӧ�ó���,���ɵ�exe�ļ������Ե�ǰ������ļ���
	#����Ķ����ļ�Ϊ��ǰ������ļ�������������main������.cpp,.c,.cc,.hpp���ļ�
	def gen_str_mfc_app_exe_tag(self,file_traits_array,file):
		self.bakefile_str=self.bakefile_str+'''	
		<exe id="'''
		#(file.split('.'))[0]Ϊ�����õ�.cpp,.c,.cc,.hpp���ļ���ǰ׺
		#��file=dictTest.cpp,����(file.split('.'))[0],�õ�����dictTest
		self.bakefile_str=self.bakefile_str+(file.split('.'))[0]+'''">
			<app-type>gui</app-type>
		'''
		
		#���gtest,cppunit,mysql,wx,mfc,��Դ�ļ��ȵ�֧��
		self.gen_str_include_lib(file_traits_array,file)
		
		#��������ǵ�ǰĿ¼������������main������.cpp,.c,.cc���ļ�
		for each_file in self.nomain_file_array:
			self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+each_file+'''"))</sources>
			'''

		#��������ǵ�ǰ������ļ�
		self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+file+'''"))</sources>
		'''
		self.bakefile_str=self.bakefile_str+'''</exe>
		'''

	########################################################################
	#�������ɶ�̬��,���ɿ���ļ������Ե�ǰĿ¼��
	def str_create_lib_tag(self,file_traits_array,file):
		self.bakefile_str=self.bakefile_str+'''
		<lib id="'''
		#app_nameΪ��ǰĿ¼�÷ָ���'\'�ָ��,�õ�������
		app_name=g_cur_dir.split(os.sep)
		self.bakefile_str=self.bakefile_str+app_name[len(app_name)-1]+'''">
		'''
		
		#���gtest,cppunit,mysql,wx,mfc,��Դ�ļ��ȵ�֧��
		self.gen_str_include_lib(file_traits_array,file)
		
		#��������ǵ�ǰĿ¼������.cpp,.c,.cc,.hpp���ļ�
		for each_file in self.nomain_file_array:
			self.bakefile_str=self.bakefile_str+'''<sources>$(fileList("'''+each_file+'''"))</sources>
		'''
		self.bakefile_str=self.bakefile_str+'''</lib>
'''
	
	########################################################################
	#�ڵ�ǰĿ¼����bakefile�ļ�
	#�ж��ļ���������,��AppӦ�ó�����ʼ����bakefile_str�ĵ�һ��ѭ��
	#ѭ���Ե�ǰĿ¼�µ����к���main���ļ����а�������,��������һ����̬��
	def create_bkl_file(self,file_traits_array):
		#�ж��ļ�����
		self.find_file_traits(file_traits_array)
		
		self.assign_main_file_array(file_traits_array)
		self.assign_nomain_file_array()
		self.assign_rc_file_array()
		self.gen_str_include_tag(file_traits_array)
		#��AppӦ�ó���,������������͵�Ӧ�ó���,������Ӧ�Ĵ���
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
		#��Lib��,���ɶ�̬��
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
			
