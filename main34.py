login = input("loginni kiriting: ")
parol = int(input("parolni kiriting: "))

if login == "ymso" and parol == 9363:
    print("to'g'ri")
elif login != "ymso" and parol == 9363:
    print("login xato")
elif login == "ymso" and parol != 9363:
    print("parol xato")