import json
import os;

json_data="""
{"age": 20, "score": 88, "name": "Bob"}
"""
if not os.path.isfile("a.json"):
    file=open("a.json","w");
    file.write(json_data);
a=open("a.json")
b=json.load(a);
print b;
print b['age'];

