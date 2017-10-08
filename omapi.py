import pypureomapi

KEYNAME="defomapi"
BASE64_ENCODED_KEY="+bFQtBCta6j2vWkjPkNFtgA=="

lease_ip = "192.168.1.77" # ip of some host with a dhcp lease on your dhcp server
dhcp_server_ip="127.0.0.1"
port = 7911 # Port of the omapi service

try:
    o = pypureomapi.Omapi(dhcp_server_ip,port, KEYNAME, BASE64_ENCODED_KEY)
    mac = o.lookup_mac(lease_ip)
    print "%s is currently assigned to mac %s" % (lease_ip, mac)
except pypureomapi.OmapiErrorNotFound:
    print "%s is currently not assigned" % (lease_ip,)
except pypureomapi.OmapiError, err:
    print "an error occured: %r" % (err,)



