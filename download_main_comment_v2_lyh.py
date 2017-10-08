# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re
import urllib,urllib2
import cookielib
import time
import os,sys
import anydbm

url_root = "http://www.jinmiao.cn/" 
path_root = "/home/"
sleep_download_time = 5

def get_html(url):
    """
	下载并保存网页内容
	间隔时间5s,防止连接时间过久导致网站认为是攻击行为而重置连接
	"""
    get_html_content = urllib.urlopen(url)
    page_content = get_html_content.read()
    get_html_content.close()
    time.sleep(sleep_download_time)
    return page_content

def first_page_list(html):
    """
	正则表达式用于匹配目录页单个页面中的文件和url列表
    """                                                    
    re_first = r"<div class='zjimage'><a (.*?)>"
    first_list = re.findall(re_first,html)
    return first_list

def get_page_num(html):
    """
	获取子页页码总数
    """	
    re_first_pagenum = re.compile(r"&nbsp;&nbsp;.*?\d/(\d+)")
    first_pagenum = re_first_pagenum.findall(html)                      
    return first_pagenum

def first_total_list(url):
    """
	获取目录页中所有的文件名和url，并存为字典
	"""
    url_list = []
    first_dict = {}
	"""
	存储第一页对应列表
	"""
    first_html = get_html(url)
    url_list.extend(first_page_list(first_html))
    num = get_page_num(first_html)
	"""
	从第二页开始存储列表，直至末页
	"""
    for pagenum in range(2,int(num[0])+1):						
#    for pagenum in range(2,4):						
        first_url_pagechange = url+"&big_type1=&age=&page="+str(pagenum)
        first_htmlpagenum = get_html(first_url_pagechange)
	    url_list.extend(first_page_list(first_htmlpagenum))
    """
	通过正则将文件名和url分离，并存入字典中
	"""
    re_first = re.compile(r"href='(.*?)'|title='(.*?)'")
    for i in range(len(url_list)):
        first_list = re_first.findall(url_list[i])
        first_dict[first_list[1][1]] = first_list[0][0]
#        print "second url:", first_list[0][0]
#        print "second dir:", first_list[1][1] 
    return first_dict

def make_dir(name):
    """
	检查目录是否存在并创建目录，切换至新建目录
	"""
#    dir_name = re.findall(re_dirname,file_content)
#    dir_name = unicode_str(dir_name[0])
    if os.path.isdir(name):
       os.chdir(name)
    else:
       os.mkdir(name)
       os.chdir(name)

def download_file(file_url,file_name,url):
	"""
	获取的三个参数分别为文件存放路径，文件名，和主页（用于获取cookie信息）
	判断文件是否存在，不存在则下载
	如果没有防盗链，直接下载。
	"""
    if os.path.isfile(file_name):
        return 1
    else:
        try:
		"""
		有防盗链的设置，则捕获HTTPError，并通过使用cookie，获取头文件信息进行下载
		"""
            f_code = urllib2.urlopen(file_url).read()
            f_mid = open(file_name,"wb")
            f_mid.write(f_code)
        except urllib2.URLError,msg:
		    """
			捕获HTTPError 500 错误并忽略，因为文件能正常下载，但是脚本会因为异常被终止，
			"""
            try:
			"""
			获取HTTP header
			"""
                cookie_j = cookielib.CookieJar()
                opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_j))
                response = opener.open(url)
                for d_item in cookie_j:
                    if d_item.name == "virtualwall":
                        cookie_value = "virtualwall="+d_item.value
#                print cookie_value
#                time.sleep(2)
                """
				访问网页时添加文件头信息
				"""
                i_headers = {"Cookie":cookie_value,"Referer":url_root}
                req = urllib2.Request(file_url,headers=i_headers)
                f_code = urllib2.urlopen(req).read()
                f_mid = open(file_name,"wb")
                f_mid.write(f_code)
            except urllib2.URLError,msg:
                pass
            finally:
			    """
				打印当前下载的文件url和文件名(finally语句段可以注释掉)
				"""
                print file_url,file_name
                return 1


def main_download_file(html,second_url,db_name):
    """
	第二级网页（含有文件存放路径的网页），
	正则匹配包含文件名的路径的字符串，
	根据保存的列表信息，通过字符串分割，分别获得文件名和文件存放路径
	将结果传给下载文件的函数
	"""
#    make_dir(file_content)
    first_dict = {}
    first_dbname = db_name+".db"
    re_filename = r'onclick="add3(.*?)"'
    file_list = re.findall(re_filename,html)
    for i in range(len(file_list)):
        str_file = file_list[i]
        file_path = str_file.split(",")
        file_url = url_root+file_path[3].strip("'").lstrip("/")
        file_name  = file_path[2].strip("'")+".mp3"
        if os.path.isfile(first_dbname):
            first_dict = anydbm.open(first_dbname,'w')
        else:
            first_dict[file_name] = file_url
    

        download_file(file_url,file_name,url_root)
    os.chdir("..")

main_dict = {}
first_list = []
"""
获取主页内容，通过正则获取几个一级网页的名字和url
"""
main_html = get_html("http://www.jinmiao.cn/index.php")
re_main = r"<a href='(.*?)</a></li>"
main_list = re.findall(re_main,main_html)
"""
因为字符串相似度高，正则匹配除的内容较多，而几个需要的内容匹配时最先匹配到，通过字符串切割获取
"""
main_list = main_list[0:7]

os.chdir(path_root)

for i in range(len(main_list)):
    """
	处理目录页的字符串内容，因为获取的字符串名字和url之间多了字符 '> 使用字符串方法replace将 '> 删除，
	同时起到将名字和url完全分开的目的，将分割后的字符串使用split转换为列表，方便通过列表的位置标识符使用
	"""
	"""
	检查字典文件是否存在，如果存在打开使用，避免二次下载时重复遍历网页
	"""
    if os.path.isfile('main_dict_db'):
        main_dict = anydbm.open('main_dict_db','w')
    else:    
        first_dir_name = main_list[i].replace("'>"," ").split()[1]
        first_url = main_list[i].replace("'>"," ").split()[0] 
        main_dict[first_dir_name] = first_url
 
"""
将目录页的名字和url对应的字典保存的本地
""" 
main_db = anydbm.open('main_dict_db','c')
for k,v in main_dict.items():
    main_db[k] = v
main_db.close()

       
for first_k in main_dict:
    make_dir(first_k)
	"""
	根据分类目录创建字典文件，保存该分类下的所有的最终文件和url
	"""
    first_dbname = first_k+'.db'
    first_url = url_root + main_dict.get(first_k)
    if os.path.isfile(first_dbname):
        first_dict = anydbm.open(first_dbname,'w')
    else:
        first_dict = first_total_list(first_url)
        first_db = anydbm.open(first_dbname,'c')
        
    first_db = anydbm.open(first_dbname,'c')
    for k,v in first_dict.items():
        first_db[k] = v
    first_db.close()    
#    for k,v in first_dict.items():
#        print k,v

    for second_k in first_dict:
	    """
		从字典中取出目录名，获得对应值(url),拼接url，传给最后的函数进行下载
		"""
        make_dir(second_k)
        second_url = url_root + first_dict.get(second_k)
        second_html = get_html(second_url)
        main_download_file(second_html,second_url,first_k)
        time.sleep(sleep_download_time)
    os.chdir(path_root)





