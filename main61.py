try:
    import time
    ism = input("ismingizni kiriting")
    familiya = input("familiyangizni kiriting")
    parol = int(input("parol kiriting"))
    login = input("login kiriting")
    e = 0
    if ism != "Oybegim" and familiya == "Sultonova" and parol == 1234 and login == "so1234":
        while e< 2:
            e += 1
            time.sleep(2)
            print(e)
    elif ism == "Oybegim" and familiya != "Sultonova" and parol ==1234 and login == "so1234":
        while e < 2:
            e += 1
            time.sleep(2)
            print(e)
    elif ism == "Oybegim" and familiya == "Sultonova" and parol != 1234 and login == "so1234":
        while e < 2:
            e += 1
            time.sleep(2)
            print(e)
    elif ism == "Oybegim" and familiya == "Sultonova" and parol == 1234 and login != "so1234":
        while e <2:
            e +=1
            time.sleep(2)
            print(e)
    elif ism != "Oybegim" and familiya != "Sultonova" and parol == 1234 and login == "so1234":
        while e < 3:
            e += 1
            time.sleep(3)
            print(e)
    elif ism == "Oybegim" and familiya != "Sultonova" and parol != 1234 and login == "so1234":
        while e < 3:
            e += 1
            time.sleep(3)
            print(e)
    elif ism == "Oybegim" and familiya == "Sultonova" and parol != 1234 and login != "so1234":
        while e <3:
            e +=1
            time.sleep(3)
            print(e)
    elif ism != "Oybegim" and familiya != "Sultonova" and parol != 1234 and login != "so1234":
        while e<4:
            e +=1
            time.sleep(4)
            print(e) 
    elif ism == "Oybegim" and familiya == "Sultonova" and parol == 1234 and login == "so1234":
        print("Tabriklaymiz siz dasturga kirdingiz")

    a = int(input("raqam kiriting"))   
except ValueError:
    print("siz str kiritdingiz")

