

import json
 
class Student(object):
  def __init__(self, name, age, score):
    self.name = name
    self.age = age
    self.score = score

def class_2_json(): 
    s = Student('Bob', 20, 88)
    #print(json.dumps(s))
    print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
  return Student(d['name'], d['age'], d['score'])
 
def dict2class()
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print(json.loads(json_str, object_hook=dict2student))
    b=json.loads(json_str, object_hook=dict2student);
    print type(b);
    print  b.age;
    print  b.name;
    print  b.score;

def json_2_dict():
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    return json.loads(json_str);

a=json_2_dict();
print a;
print a['age'];

    
