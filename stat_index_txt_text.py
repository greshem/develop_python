#coding:gbk
# ------------------------------------------------------------
# 简介 : 从一个文件中选出使用频率最多的10个单词
#       请自行准备一个 test.txt 文档放在与本脚本相同目录
# 更新 : 2008年6月27日
# ------------------------------------------------------------

from time import time
from operator import itemgetter

def test():
    # 取 10 个，有需要可以修改, 及定义读取的文件 test.txt 
    iList = 10
    strFileName = '/etc/passwd'

    count = {}
    for word in open(strFileName).read().split():
        if count.has_key(word):
            count[word] = count[word] + 1
        else:
            count[word] = 1
    print sorted(count.iteritems( ), key=itemgetter(1), reverse=True)[0:iList]

# 调用
if __name__ == '__main__':
    t1 = time()
    test()
    print time()-t1

