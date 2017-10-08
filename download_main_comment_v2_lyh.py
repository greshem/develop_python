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
	���ز�������ҳ����
	���ʱ��5s,��ֹ����ʱ����õ�����վ��Ϊ�ǹ�����Ϊ����������
	"""
    get_html_content = urllib.urlopen(url)
    page_content = get_html_content.read()
    get_html_content.close()
    time.sleep(sleep_download_time)
    return page_content

def first_page_list(html):
    """
	������ʽ����ƥ��Ŀ¼ҳ����ҳ���е��ļ���url�б�
    """                                                    
    re_first = r"<div class='zjimage'><a (.*?)>"
    first_list = re.findall(re_first,html)
    return first_list

def get_page_num(html):
    """
	��ȡ��ҳҳ������
    """	
    re_first_pagenum = re.compile(r"&nbsp;&nbsp;.*?\d/(\d+)")
    first_pagenum = re_first_pagenum.findall(html)                      
    return first_pagenum

def first_total_list(url):
    """
	��ȡĿ¼ҳ�����е��ļ�����url������Ϊ�ֵ�
	"""
    url_list = []
    first_dict = {}
	"""
	�洢��һҳ��Ӧ�б�
	"""
    first_html = get_html(url)
    url_list.extend(first_page_list(first_html))
    num = get_page_num(first_html)
	"""
	�ӵڶ�ҳ��ʼ�洢�б�ֱ��ĩҳ
	"""
    for pagenum in range(2,int(num[0])+1):						
#    for pagenum in range(2,4):						
        first_url_pagechange = url+"&big_type1=&age=&page="+str(pagenum)
        first_htmlpagenum = get_html(first_url_pagechange)
	    url_list.extend(first_page_list(first_htmlpagenum))
    """
	ͨ�������ļ�����url���룬�������ֵ���
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
	���Ŀ¼�Ƿ���ڲ�����Ŀ¼���л����½�Ŀ¼
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
	��ȡ�����������ֱ�Ϊ�ļ����·�����ļ���������ҳ�����ڻ�ȡcookie��Ϣ��
	�ж��ļ��Ƿ���ڣ�������������
	���û�з�������ֱ�����ء�
	"""
    if os.path.isfile(file_name):
        return 1
    else:
        try:
		"""
		�з����������ã��򲶻�HTTPError����ͨ��ʹ��cookie����ȡͷ�ļ���Ϣ��������
		"""
            f_code = urllib2.urlopen(file_url).read()
            f_mid = open(file_name,"wb")
            f_mid.write(f_code)
        except urllib2.URLError,msg:
		    """
			����HTTPError 500 ���󲢺��ԣ���Ϊ�ļ����������أ����ǽű�����Ϊ�쳣����ֹ��
			"""
            try:
			"""
			��ȡHTTP header
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
				������ҳʱ����ļ�ͷ��Ϣ
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
				��ӡ��ǰ���ص��ļ�url���ļ���(finally���ο���ע�͵�)
				"""
                print file_url,file_name
                return 1


def main_download_file(html,second_url,db_name):
    """
	�ڶ�����ҳ�������ļ����·������ҳ����
	����ƥ������ļ�����·�����ַ�����
	���ݱ�����б���Ϣ��ͨ���ַ����ָ�ֱ����ļ������ļ����·��
	��������������ļ��ĺ���
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
��ȡ��ҳ���ݣ�ͨ�������ȡ����һ����ҳ�����ֺ�url
"""
main_html = get_html("http://www.jinmiao.cn/index.php")
re_main = r"<a href='(.*?)</a></li>"
main_list = re.findall(re_main,main_html)
"""
��Ϊ�ַ������ƶȸߣ�����ƥ��������ݽ϶࣬��������Ҫ������ƥ��ʱ����ƥ�䵽��ͨ���ַ����и��ȡ
"""
main_list = main_list[0:7]

os.chdir(path_root)

for i in range(len(main_list)):
    """
	����Ŀ¼ҳ���ַ������ݣ���Ϊ��ȡ���ַ������ֺ�url֮������ַ� '> ʹ���ַ�������replace�� '> ɾ����
	ͬʱ�𵽽����ֺ�url��ȫ�ֿ���Ŀ�ģ����ָ����ַ���ʹ��splitת��Ϊ�б�����ͨ���б��λ�ñ�ʶ��ʹ��
	"""
	"""
	����ֵ��ļ��Ƿ���ڣ�������ڴ�ʹ�ã������������ʱ�ظ�������ҳ
	"""
    if os.path.isfile('main_dict_db'):
        main_dict = anydbm.open('main_dict_db','w')
    else:    
        first_dir_name = main_list[i].replace("'>"," ").split()[1]
        first_url = main_list[i].replace("'>"," ").split()[0] 
        main_dict[first_dir_name] = first_url
 
"""
��Ŀ¼ҳ�����ֺ�url��Ӧ���ֵ䱣��ı���
""" 
main_db = anydbm.open('main_dict_db','c')
for k,v in main_dict.items():
    main_db[k] = v
main_db.close()

       
for first_k in main_dict:
    make_dir(first_k)
	"""
	���ݷ���Ŀ¼�����ֵ��ļ�������÷����µ����е������ļ���url
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
		���ֵ���ȡ��Ŀ¼������ö�Ӧֵ(url),ƴ��url���������ĺ�����������
		"""
        make_dir(second_k)
        second_url = url_root + first_dict.get(second_k)
        second_html = get_html(second_url)
        main_download_file(second_html,second_url,first_k)
        time.sleep(sleep_download_time)
    os.chdir(path_root)





