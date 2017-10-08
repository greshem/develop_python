from random import choice;
from mysql_db  import get_mysql_session;

def get_all_user():
    session = get_mysql_session("billing");
    rows=session.execute('select * from  account  ;').fetchall();
    users= [ each['user_id']    for each in  rows ];
    session.close();
    return users;


def add_one_user(id, name ):
	account_id=id;
	username=name;
	cash_balance=100;
	gift_balance=200;
	type_=choice(["credit",None]);
	credit_line=2000;
	status=choice(["delete", "delete", "freezing"]);
	#created_at;
	#updated_at=row['updated_at'];
	session = get_mysql_session("keystone");
	
	sql_str="""
INSERT INTO `billing`.`account` (`account_id`, `username`, `cash_balance`, `gift_balance`, `type`, `credit_line`, `status`, `created_at`, `updated_at`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%s',  NULL, NULL);
"""%(account_id, username, cash_balance, gift_balance, type_, credit_line, status);
	print sql_str;
	session.execute(sql_str);
	session.commit();
	session.close();


def sync_from_keystone():
    session = get_mysql_session("keystone");
    for row in session.execute('select * from  user   ;').fetchall():
        row=dict(zip(row.keys(), row.values()));
        id=row['id'];
        name=row['name'];

        print "id=%s\n"%id;
        print "name=%s\n"%name;
        add_one_user(id, name);

def  random_gen_user():
    import random;
    number=int(random.uniform(0,9999));
    add_one_user("%032d"%number, "name%s"%number);

if __name__=="__main__":
    #sync_from_keystone();
    print get_all_user();


    #number=1;
    #add_one_user("%032d"%number, "name%s"%number);


