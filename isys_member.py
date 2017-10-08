#!/usr/bin/python

import os
import sys

# for testing
# if (os.path.exists('isys')):
#     sys.path.append('isys')


#['EARLY_SWAP_RAM', 'MIN_GUI_RAM', 'MIN_RAM', '__builtins__', '__doc__', '__file__', '__name__', '_isys', '_readFATLabel',
# 'auditDaemon', 'bind_textdomain_codeset', 'biosdisks', 'block', 'cachedDrives', 'cdRwList', 'cdromList', 
# 'checkBoot', 'chroot', 'classMap', 'compareDrives', 'compareNetDevices', 'configNetDevice', 'd', 'ddfile', 
# 'deviceIsReadOnly', 'dhcpNetDevice', 'disk', 'doGetBiosDisk', 'doProbeBiosDisks', 'driveDict', 'driveIsIscsi', 
# 
# 'driveUsesModule', 'ejectCdrom', 'ext2Clobber', 'ext2HasJournal', 'ext2IsDirty', 'fbconProbe', 'fbinfo', 
# 'floppyDriveDict', 'flushDriveDict', 'fsSpaceAvailable', 'getDasdDevPort', 'getDasdPorts', 'getDasdState', 
# 'getIPAddress', 'getLinkStatus', 'getMacAddress', 'getMpathModel', 'getRaidChunkFromDevice', 'getopt', 
# 'handleSegv', 'hardDriveDict', 'htavailable', 'ideCdRwList', 'inet_calcNetBroad', 'isIsoImage', 'isLdlDasd', 
# 'isPAE', 'isPaeAvailable', 'isPsudoTTY', 'isUsableDasd', 'isVioConsole', 'isWireless', 'iutil', 'kudzu', 
# 'loadFont', 'loadKeymap', 'lochangefd', 'log', 'logging', 'losetup', 'makeDevInode', 'makedev', 'mediaPresent', 
# 'mknod', 'mount', 'mountCount', 'netmask2prefix', 'os', 'pathSpaceAvailable', 'posix', 'prefix2netmask', 
# 'printObject', 'raidCount', 'raidsb', 'raidsbFromDevice', 'raidstart', 'raidstop', 're', 'readExt2Label', 
# 'readFATLabel', 'readFSLabel', 'readJFSLabel', 'readJFSLabel_int', 'readReiserFSLabel', 'readReiserFSLabel_int', 
# 'readSwapLabel', 'readSwapLabel_int', 'readXFSLabel', 'readXFSLabel_int', 'resetFileContext', 'resetResolv', 
# 'resource', 'rhpl', 'setResolvRetry', 'smpAvailable', 'socket', 'spaceAvailable', 'string', 'struct',
#  'swapoff', 'swapon', 'sync', 'sys', 'tapeDriveList', 'umount', 'unlosetup', 'vtActivate', 'warnings', 
# 'wipeRaidSB']

sys.path.append('/usr/lib/anaconda')

import isys
print dir("isys");
print dir(isys);
#isys.rmrf("/tmp/c");
isys.sync();

