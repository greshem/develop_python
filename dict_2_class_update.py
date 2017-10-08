class Lpar:
    def __init__(self, **entries):
        self.__dict__.update(entries)


meta=['id', 'name', 'status', 'time', 'memory', 'cpu','unit','led'];
value=["39","FF_lpar39","Running","13d","2048M","0.80","4"];

line=Lpar(**dict(zip(meta, value)));
print line;
