import commands
import os
import string
import sys
from os.path import join, getsize
import re;



for root, dirs, files in os.walk("/root/bin"):
    for file in files:
        abs_path = os.path.join(root,file)
        py=re.compile('py');
        if  py.search(abs_path):
            print abs_path;
