import os;
from  itertools  import * ;



def file_to_array_array(file):
    array=[]
    for line in open(file).readlines() :
        array.extend(line.split() );
    return array;


for each in  file_to_array_array("/etc/passwd"):
    print each;
