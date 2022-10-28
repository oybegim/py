login = input("login kiriting ")
parol = input("parol kiriting ")

if login != "abc":
    print("loginni xato kiritdingiz")
elif login == "abc":
    print("login to'g'ri")
elif parol == "1234":
    print("parolni to'g'ri kiritdingiz")
elif parol != "1234":
    print("parolni xato kiritdingiz")
else:
    print("siz dasturga kira olmadingiz")
