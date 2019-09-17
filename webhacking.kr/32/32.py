import requests


url = "http://webhacking.kr/challenge/codeing/code5.html"

params = {
	"hit":"freakout"
}
headers = {
"Cookie":"PHPSESSID=8aa8b01919b86d9a80f524a71c187ce9",
"Host":"webhacking.kr"
	
}
for i in range(1,100):
	req = requests.get(url, params=params, headers = headers)
	print req.content