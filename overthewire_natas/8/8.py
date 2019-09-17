import base64

hexdecode = '3d3d516343746d4d6d6c315669563362'.decode('hex')
print "\'3d3d516343746d4d6d6c315669563362\' hexdecode  : ",hexdecode,"\n"

strrev = ''.join(reversed(hexdecode))
print "strrev : ",strrev,"\n"

secret = base64.b64decode(strrev)

print "secret : ",secret