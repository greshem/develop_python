#coding:gbk
# ------------------------------------------------------------
# ��� : ��һ���ļ���ѡ��ʹ��Ƶ������10������
#       ������׼��һ�� test.txt �ĵ������뱾�ű���ͬĿ¼
# ���� : 2008��6��27��
# ------------------------------------------------------------

from time import time
from operator import itemgetter

def test():
    # ȡ 10 ��������Ҫ�����޸�, �������ȡ���ļ� test.txt 
    iList = 10
    strFileName = '/etc/passwd'

    count = {}
    for word in open(strFileName).read().split():
        if count.has_key(word):
            count[word] = count[word] + 1
        else:
            count[word] = 1
    print sorted(count.iteritems( ), key=itemgetter(1), reverse=True)[0:iList]

# ����
if __name__ == '__main__':
    t1 = time()
    test()
    print time()-t1

