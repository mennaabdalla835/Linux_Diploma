users={"ahmed": "1394", "ali": "6078", "amr":"9345"}

username = input(" enter your name \n")
password = input(" enter your password \n")

if username in users and users[username]==password:
    print("hello " + username)
else:
    print("incorrect entery")