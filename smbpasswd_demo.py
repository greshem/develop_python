import smbpasswd

passwd = 'mypassword'

#print 'LANMAN hash is', smbpasswd.lmhash(passwd)
print 'NT hash is', smbpasswd.nthash(passwd)

print 'both hashes at once = %s:%s' % smbpasswd.hash(passwd)
