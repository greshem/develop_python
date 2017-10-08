#!/usr/bin/python
import rpmUtils.arch; 
print rpmUtils.arch.getBaseArch(myarch=rpmUtils.arch.getCanonArch(skipRpmPlatform = True));
