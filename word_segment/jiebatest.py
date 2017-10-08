#encoding=utf-8
import jieba

if __name__ == '__main__':
    
    line = '我真是醉了'
    
    seg_list = jieba.cut(line)
    seg_list = " ".join(seg_list)
    print seg_list