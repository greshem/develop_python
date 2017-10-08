def  get_mysql_session(db):
    from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
    from sqlalchemy.orm import sessionmaker
    import ConfigParser


    config_read = ConfigParser.RawConfigParser()
    config_read.read('config.ini')
    mysql_server=config_read.get('global','mysql_server')
    mysql_user=config_read.get('global','mysql_user')
    mysql_pass=config_read.get('global','mysql_password')

    
    DB_CONNECT_STRING = 'mysql+mysqldb://%s:%s@%s:3307/%s?charset=utf8'%( mysql_user, mysql_pass, mysql_server,db);
    engine = create_engine(DB_CONNECT_STRING, echo=True)
    DB_Session = sessionmaker(bind=engine)
    session = DB_Session()
    return session;


if __name__=="__main__":
    session = get_mysql_session("mysql");
    for row in session.execute('select * from  user  ;').fetchall():
        row=dict(zip(row.keys(), row.values()));
        print row;
        #print row['User'],
        #print row['Password']


