
import mechanize  
import cookielib  
  
  
br = mechanize.Browser()  
cj = cookielib.LWPCookieJar()  
br.set_cookiejar(cj)  
br.set_handle_equiv(True)  
br.set_handle_gzip(True)  
br.set_handle_redirect(True)  
br.set_handle_referer(True)  
br.set_handle_robots(False)  
  
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)  
br.set_debug_http(False)  
  
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1')]  
  
response = br.open('http://xxxx/signon')  
br.select_form(name='loginFrm')  
br.form['userName'] = 'xxx'  
br.form['password'] = 'yyy'  
br.submit()  
print 'login successful!'  
response = br.open('http://xxxx/app/application/attendmanage/vieworiginaldata.jsp')  
br.select_form(name='form1')  
br.form.set_all_readonly(False)  
br.form.action = 'http://xxxx/app/servlet/ViewOriginalDataServlet'  
br.form['fromdate'] = '2012-09-05'  
br.submit()  
print br.response().read()  
