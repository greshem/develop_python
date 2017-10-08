class blacklast:
    db=None;
    col=None;
    def __init__(self):
        db="test";
        col="col";

    def db_name(self, db_name):
        self.db=db_name;

    def col_name(self, col_name):
        self.col=col_name;
    
    def dump(self):
        print self.db;
        print self.col;

    def norm(self):
        self.db_name("aaaaaaa");
        self.col_name("bbbbb");


    def norm2(self):
        self.db="222222";
        self.col="33333";


    def norm3(self):
        db="##########";
        col="==============";

if __name__=="__main__":
    a=blacklast();
    a.dump();

    a.db_name("db_name");
    a.col_name("col_name");
    a.dump();

    a.norm();
    a.dump();


    a.norm2();
    a.dump();

    a.norm3();
    a.dump();
