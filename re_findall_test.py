
def re_find_all():
    import re;
    size_str=" Size: 33333\n";
    size=re.findall(r'\s+Size: (.*)\n',size_str)
    print size;
