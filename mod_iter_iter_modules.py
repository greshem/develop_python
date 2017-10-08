import pkgutil;

for importer, name, ispkg in pkgutil.iter_modules(["./"]):
    print "%s :  %s : %s" %(importer,name,ispkg);
