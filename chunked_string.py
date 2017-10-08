from boltons.iterutils import  chunked;

a="a"*1000;
print a;


all_data=chunked(a, 10)

print all_data[-1];


