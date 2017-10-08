
import os
import sys

def is_mfc_platform(dir_array):
	for path in dir_array:
		if path.endswith(".h"):
			if path=="StdAfx.h":
				return 1
	return 0

def create_bkl():
	build_data='''<?xml version="1.0" ?>
<!-- $Id: bakefile_quickstart.txt,v 1.5 2006/02/11 18:41:11 KO Exp $ -->

<makefile>
    
    <include file="presets/wx.bkl"/>
        <exe id="'''
	dir=os.getcwd()
	path=dir.split(os.sep)
	build_data=build_data+path[len(path)-1]
	wx_data='''">
	<app-type>console</app-type>
	<define>wxUSE_OLE</define>
	<define>WXUSINGDLL</define>
	<cxxflags>/D_UNICODE</cxxflags>
	<cxxflags>/D__WXMSW__</cxxflags>
	<cxxflags>/DWINDOWSCODE</cxxflags>
	<cxxflags>/D__WXDEBUG__</cxxflags>
	<cxxflags>/MTd</cxxflags>
	<include>D:\usr\include</include>
	<include>D:\usr\include\msvc</include>
	<include>D:\usr\include\lmyunit</include>
	<lib-path>D:\usr\lib</lib-path>
	<sys-lib>UnitCode</sys-lib>
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
	mfc_data='''">
	<app-type>console</app-type>
	<cxxflags>/DWINDOWSCODE</cxxflags>
	<include>D:\usr\include\lmyunit</include>
		<lib-path>D:\usr\lib</lib-path>
		<sys-lib>UnitCode</sys-lib>
	<cxxflags>/D_AFXDLL</cxxflags> 
	<cxxflags>/D_MBCS</cxxflags>
	<cxxflags>/MDd</cxxflags>
	<ldflags>/INCREMENTAL:NO</ldflags>
	<ldflags>/NOLOGO</ldflags>
	<ldflags>/NODEFAULTLIB:LIBCMTD.lib</ldflags>
	<ldflags>/DEBUG</ldflags>
	<ldflags>/SUBSYSTEM:WINDOWS</ldflags>
	<ldflags>/MACHINE:X86</ldflags>
	'''
	data='''<cxxflags>/DWIN32</cxxflags>
			<cxxflags>/D_DEBUG</cxxflags>			
			<cxxflags>/D_WINDOWS</cxxflags>
			<cxxflags>/DNOPCH</cxxflags>   
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
			<sources>$(fileList('*.cpp'))</sources> 
        </exe>


</makefile>'''
	f=open("build.bkl","wt")
	dir_array=os.listdir(dir)
	res=''
	for path in dir_array:
		if path.endswith(".rc"):
			res='''<win32-res>'''+path+'''</win32-res>
			'''		
			break
	
	if 1==is_mfc_platform(dir_array):
		build_data=build_data + mfc_data + res + data
	else:
		build_data=build_data + wx_data + res + data
	f.write(build_data)
	f.close()


if "clean"==sys.argv[len(sys.argv)-1]:
	os.system("nmake /f makefile.vc clean")
else:
	create_bkl()

	if 0!=os.system("bakefile -f msvc build.bkl"):
		print "bakefile -f msvc build.bkl failed, please check"
		sys.exit(1)
	if 0!=os.system("nmake /f makefile.vc"):
		print "nmake /f makefile.vc failed, please check"
		sys.exit(2)
