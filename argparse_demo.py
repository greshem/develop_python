
from pymongo import MongoClient
import re;
import argparse
 
def parse_args():

    description = """
    Usage: %prog [options];

    Example:
        python  %prog   --db  domain --col  email  --field  domain   whitep

"""
    parser = argparse.ArgumentParser(description = description)

    help = """pattern """;
    parser.add_argument('pattern',help=help)

    help = """mongodb db """
    parser.add_argument('-d','--db', help=help, default='domain')


    help = """mongodb col """
    parser.add_argument('-c','--col', help=help, default='domain')

    help = """mongodb col's field  """
    parser.add_argument('-f','--field', help=help, default='domain')

    args = parser.parse_args();
    return args

if __name__ == '__main__':
    args = parse_args()
    print "The db is :%s"%args.db;
    print "The col is :%s"%args.col;

    print "The pattern is :%s"%args.pattern;


    client = MongoClient("localhost", 27017);
    db = client[args.db];
    col = db[args.col];
    
    pat=re.compile(".*%s"%args.pattern);
    for each2 in col.find({"%s"%args.field:pat}):
        print each2['%s'%args.field];

