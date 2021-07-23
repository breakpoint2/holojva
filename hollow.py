passwords = {"usr1": "password", "usr2": "lol", "usr3": "another_pwd"}
messages = {"usr1": [], "usr2": [], "usr3": []}
while True :   
    while True :
        login = input("Login? ")
        password = input("Password? ")
        if passwords[login] != password :
            print("Try another password")
        else:
            break
    def write(messages) :
        while True :
            user = input("Choose user? ")
            if user in passwords.keys() :
                message = input("Message? ")
                messages[user].append([login, message])
                break
            else :
                print("This user does not exist")
    def look() :
        for i in messages[login] :
            print(i)
    while True :
        hello = input("'write' to write message, 'look' to look to messages, 'unlogin' to unlogin ")
        if hello == "write" :
            write(messages)
        if hello == "look" :
            look()
        if hello == "unlogin" :
            break