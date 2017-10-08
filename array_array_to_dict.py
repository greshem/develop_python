
meta=['id', 'name', 'status', 'time', 'memory', 'cpu','unit','led'];
date=[ 1  ,  2,     3      ,  4    , 5       ,  6   , 7    , 8 ];

a=dict(zip(meta, date));
print a;
print a['id'];

