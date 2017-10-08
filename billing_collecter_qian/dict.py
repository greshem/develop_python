
a = db.execute('select * from acquisizioni_motes')
b = a.fetchall()
c = b[0]

# and now, finally...
dict(zip(c.keys(), c.values()))

dictlist = [dict(row) for row in somequery.execute().fetchall()]
