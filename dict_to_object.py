def method_1():
    info={'status': 'Running', 'led': '', 'name': '10-597BR', 'time': '57d', 'id': '1', 'memory': '8192M', 'cpu': '0.80', 'unit': '8'}
    print info;

    def _dict_to_object(d):
        class _O: pass
        [setattr(_O, _k, d[_k]) for _k in d]
        return _O

    lpar=_dict_to_object(info);
    print dir(lpar);
    print lpar.name;
    print lpar.id;
    print lpar.time;
    #print lpar.time3;




def method_2():
    print "#=========\n";
    class Lpar2:
        def __init__(self, **entries):
            self.__dict__.update(entries)
     
    info={'status': 'Running', 'led': '', 'name': '10-597BR', 'time': '57d', 'id': '1', 'memory': '8192M', 'cpu': '0.80', 'unit': '8', "testing":333}
    r = Lpar2(**info)
    print r.name;
    print r.testing;


method_2();
