#encoding=utf-8
from sys import argv
import jieba
import os;

if __name__ == '__main__':
    
    emotionDictionary = {} 
    result = 0
    if not  os.path.isfile("BosonNLP_sentiment_score.txt"):
        print "file:  BosonNLP_sentiment_score.txt not exists \n";
        print "copy from   4T grehsem  \n";
        print "K:\sdb1\_xfile\\2016_all_iso\_xfile_2016_02\情感_检测\ \n";
        os.exit(1);
    
    file_object = open('BosonNLP_sentiment_score.txt')
    try:
        lines = file_object.readlines()
        for line in lines:
           # print type(lines)   
            words = line.split(' ')
            if len(words) <2:
                continue
            emotionDictionary[words[0]] = words[1]        
    finally:
        file_object.close( )

    #word_input = '我踩屎了'
    word_input = argv[1]
    seg_list = jieba.cut(word_input)
    seg_list = " ".join(seg_list)
    words = seg_list.split(' ')
    for word in words:
        word = word.encode('utf-8')
        if word in emotionDictionary:
            result += float(emotionDictionary[word])
    print result
    if result > 0:
        print '积极正面的'
    else:
        print '消极的'
            
