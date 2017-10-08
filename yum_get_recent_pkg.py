import yum
import yum.Errors
from yum.misc import getCacheDir
from yum.comps import Comps, CompsException
from yum.Errors import RepoMDError
import sys
import os
import libxml2
import time
from optparse import OptionParser

class YumQuiet(yum.YumBase):
    def __init__(self):
        yum.YumBase.__init__(self)
    
    def getRecent(self, days=1):
        """return most recent packages from sack"""

        recent = []
        now = time.time()
        recentlimit = now-(days*86400)
        ftimehash = {}
        if self.conf.showdupesfromrepos:
            avail = self.pkgSack.returnPackages()
        else:
            avail = self.pkgSack.returnNewestByNameArch()
        
        for po in avail:
            ftime = int(po.returnSimple('filetime'))
            if ftime > recentlimit:
                if not ftimehash.has_key(ftime):
                    ftimehash[ftime] = [po]
                else:
                    ftimehash[ftime].append(po)

        for sometime in ftimehash.keys():
            for po in ftimehash[sometime]:
                recent.append(po)
        
        return recent

