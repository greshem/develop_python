import os
if hasattr(os, "uname"):
    print os.uname();    

GRESHEM=3333;
if not hasattr(os, "uname22"):
    tmp=getattr(os, "uname");
    setattr(os, "uname22", tmp)
    setattr(os, "GRESHEM", GRESHEM)
    print os.uname22();
    print os.GRESHEM;
