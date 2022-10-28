a = ["jjhejh", "jdebb", "nnn", ["sos", "sos","raqamlardan birini tanlang 1. 2. 3    "]]
b = int(input(a[3][2]))
if b == 1:
    x = int(input("1-sonni kiriting: "))
    y = int(input("2-sonni kiriting: "))
    amal = input("amalni kiriting: ")
    if  amal == "+":
        print(x + y)
    elif amal == "-":
        print(x - y)
    elif amal == "*":
        print(x * y)
    elif amal == "/":
        print(x / y)

elif b == 2:
    login = input("loginni kiriting: ")
    parol = int(input("parolni kiriting: "))
    if login == "so" and parol == 9363:
        print("to'g'ri")
    elif login != "so" and parol == 9363:
        print("login xato")
    elif login == "so" and parol != 9363:
        print("parol to'g'ri")
    
elif b == 3:
    class Gul:
        def __init__(self, nomi, hidi):
            self.nomi = nomi
            self.hidi = hidi 
    g1 = Gul("so","zor")
    print(g1.nomi,g1.hidi)

