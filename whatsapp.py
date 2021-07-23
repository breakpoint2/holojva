passwords = {"kostya": "password", "valia": "lol", "dedushka": "6252485"}
messages = {"kostya": [], "valia": [], "dedushka": []}
while True :   
    while True :
        login = input("Логин? ")
        password = input("Пароль? ")
        if passwords[login] != password :
            print("Неверный пароль")
        else:
            break
    def write(messages) :
        while True :
            user = input("Кому ты хочешь написать? ")
            if user in passwords.keys() :
                message = input("Сообщение? ")
                messages[user].append([login, message])
                break
            else :
                print("Нет такого пользователя")
    def look() :
        for i in messages[login] :
            print(i)
    while True :
        hello = input("'write' чтобы написать сообщение, 'look' чтобы посмотреть сообщения, 'unlogin' чтобы выйти ")
        if hello == "write" :
            write(messages)
        if hello == "look" :
            look()
        if hello == "unlogin" :
            break