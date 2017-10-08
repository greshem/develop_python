
from pymongo import MongoClient

client = MongoClient("localhost", 27017);
db = client["test"];
col= db['html'];

item={};
item['a']="bbb";
item['bbbb']="bbb";
item['cbbb']="bbb";
item['content']= all_the_text = open('/etc/passwd').read( )     ;
col.insert(dict(item));
client.close();

