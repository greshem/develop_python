import commands
import os
import string
import sys
from os.path import join, getsize

for root, dirs, files in os.walk("/root/bin"):
    for file in files:
        abs_path = os.path.join(root,file)
        print abs_path;
