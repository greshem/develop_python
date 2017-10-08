import codecs
import glob
import os
import re
import subprocess
import sys


def get_baseline(fn):
    name = get_baseline_name(fn)
    f = codecs.open(name, mode='r', encoding='utf8')
    out = f.read()
    f.close()
    return out


