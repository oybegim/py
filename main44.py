ism = input("ismingizni kiriting: ")
familiya = input("familiyangizni kiriting: ")
parol = int(input("parol kiriting: "))

if ism != "Gulbodom" and familiya == "Mahammadiyeva" and parol == 1234:
    print("ism xato")
elif ism == "Gulbodom" and familiya != "Mahammadiyeva" and parol == 1234:
    print("familiya xato")
elif ism == "Gulbodom" and familiya == "Mahammadiyeva" and parol != 1234:
    print("parol xato")
elif ism != "Gulbodom" and familiya != "Mahammadiyeva" and parol == 1234:
    print("ism va familiyani xato kiritdingiz")
elif ism == "Gulbodom" and familiya != "Mahammadiyeva" and parol != 1234:    
    print("parol va familiyani xato kiritdingiz")
elif ism != "Gulbodom" and familiya == "Mahammadiyeva" and parol != 1234:
    print("parol va ismni xato kiritdingiz")
else:
    print("tabriklaymiz siz dasturga kirdingiz")