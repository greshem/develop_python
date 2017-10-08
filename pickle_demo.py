#nltk have so much  file type link pickle 

# Dump pickled tokenizer
import pickle
#out = open("slovene.pickle","wb")
#out = open("/root/.functioncache/root/bin/function_cache.py.cache","wb")
#test=None;
a= pickle.load(open("/root/.functioncache/root/bin/function_cache.py.cache", "rb"))
#a= pickle.load("/root/.functioncache/root/bin/function_cache.py.cache")
print a;

#out.close()

