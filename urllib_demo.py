from urllib import urlopen
url = 'http://www.tripadvisor.com/Restaurant_Review-g294217-d3639657-Reviews-Trattoria_Caffe_Monteverdi-Hong_Kong.html'
html = urlopen(url).read()
#html string 
print type(html);
