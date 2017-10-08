import filecmp
a=filecmp.dircmp("/root/bin/", "/bin");
a.report();
