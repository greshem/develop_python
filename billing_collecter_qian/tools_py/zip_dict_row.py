def  get_tables(session):
    row=session.execute('show tables;   ;').fetchall();
    return row
	
        #a=dict(zip(row.keys(), row.values()));
        #print a;
        #print row.keys();

