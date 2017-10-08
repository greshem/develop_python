
#1.替换所有匹配的子串用newstring替换subject中所有与正则表达式regex匹配的子串
result, number = re.subn(regex, newstring, subject) 

#2.替换所有匹配的子串（使 用正则表达式对象）
rereobj = re.compile(regex)  
result, number = reobj.subn(newstring, subject)字符串拆分 
