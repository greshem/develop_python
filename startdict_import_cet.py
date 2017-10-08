

def get_mongo_client():
    from pymongo import MongoClient
    client = MongoClient("localhost", 27017);
    db = client["english"];
    col=db['xdict'];
    return col;

def exist_in_mongo(col, word):
    if word==None:
        return None;
    ret=col.find_one({"word":word});
    return ret;

def insert_to_mongo(col, word,chinese,source="xdict"):
    item={};
    item['word']=word;
    item['chinese']=chinese;
    item['source']=source;

    col.insert(item);


def load_file():
    words=[];
    #for each in open("/root/foreign_trade_management_sys/flask_v2/data/cet4_4500.txt").readlines():
    for each in open("/root/foreign_trade_management_sys/flask_v2/data/cet6.txt").readlines():
    #for each in open("/root/foreign_trade_management_sys/flask_v2/data/hongbao_caogao.txt").readlines():
        array=each.strip().split("|");
        word=array[1];
        chinese=array[2];
        #print "%s|%s"%(word, chinese);
        tmp={};
        tmp['word']=word;
        tmp['chinese']=chinese;
        tmp['source']=['cet6']
        words.append(tmp);
    return words;


if __name__=="__main__":
    
        

    
    col=get_mongo_client();
    words=load_file();
    for each in words:
        if each==None:
            continue;
        #print each;
        ret=exist_in_mongo(col, each['word']);
        if  ret != None:
            pass;
            #print "love  in  xdict ";
        else:
            print "%s should  insert ->%s "%(each['word'], each['chinese']);
            insert_to_mongo(col, each['word'], each['chinese'], each['source']);
