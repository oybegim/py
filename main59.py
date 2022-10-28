q = int(input("raqamlardan birini tanlang: 1.string, 2.integer, 3.float, 4.boolean, 5.list"))
if q == 1:
    print("siz tekstga kirdingiz")
    w = int(input("raqamlardan birini tanlang: 1 va 2"))
    if w == 1:
        class Odam:
            def __init__(self, ism, familiya, yosh):
                self.ism = ism
                self.familiya = familiya
                self.yosh = yosh
        o1 = Odam("Oybegim", "Sultonova", 18)
        print(o1.ism, o1.familiya, o1.yosh)
    elif w == 2:
        ism = input("ismingizni kiriting")
        familiya = input("familiyangizni kiriting")
        login = input("login kiriting")
        parol = int(input("parol kiriting"))
        if ism == "Oybegim":
            print("ism to'g'ri")
        elif familiya == "Sultonova":
            print("familiya to'g'ri")
        elif login == "so":
            print("login to'g'ri")
        elif parol == 1234:
            print("parol to'g'ri")
elif q == 2:
    print("siz integer ma'lumot turiga kirdingiz")
    e = int(input("raqamlardan birini tanlang: 1.kalkulyator, 2.toq sonlar, 3.juft sonlar, 4.ikkita nol bn tugaydigan sonlar"))
    if e == 1:
        r = int(input("1-sonni kiriting"))
        t = int(input("2-sonni kiriting"))
        amal = input("amal kiriting")
        if amal == "-":
            print(r-t)
        elif amal == "+":
            print(r+t)
        elif amal == "/":
            print(r/t)
        elif amal == "*":
            print(r*t)
    elif e == 2:
        y = -1
        while y < 99:
            y += 2
            print(y)
    elif e == 3:
        u = 0
        while u < 100:
            u += 2
            print(u)
    elif e == 4:
        i = 0
        while i <9900:
            i += 100
            print(i)
elif q == 3:
    print("siz float ma'lumot turiga kirdingiz")
    o = int(input("raqamlardan birini tanlang: 1 va 2"))
    if o == 1:
        p = int(input("sonni kiriting"))
        a = int(input("darajani kiriting"))
        print(p**a)
    elif o == 2:
        s = 0
        for x in range(9):
            s += 1
            print(s)
elif q == 4:
    print("siz boolean ma'lumot turiga kirdingiz")
    try:
        f = int(input("raqam kiriting"))
    except ValueError:
        print("siz str kiritdingiz")
elif q == 5:
    print("siz list ma'lumot turiga kirdingiz")
g = int(input("raqamlardan birini tanlang: 1, 2"))
if g ==1:
    class Meva:
        def __init__(self, nomi, tami, rangi):
            self.nomi= nomi
            self.tami = tami
            self.rangi = rangi
    m1 = Meva("Anor", "tami zo'r,", "rangi qizil")
    print(m1.nomi, m1.tami, m1.rangi)
elif g ==2:
    class Tel:
        def __init__(self, rusumi):
            self.rusumi = rusumi
        def __str__(self):
            return f"{self.rusumi}"
    class Phone(Tel):
        def __init__(self, rusumi, narxi):
            super().__init__(rusumi)
            self.narxi =narxi
        def phone1(self):
            print(self.rusumi, self.narxi)
    p1 = Phone("Redmi", 1600)
    class Iphone(Tel):
        def __init__(self, rusumi, xotirasi):
            super().__init__(rusumi)
            self.xotirasi = xotirasi
        def iphone2(self):
            print(self.rusumi, self.xotirasi)
    i2 = Iphone("Iphone14", 128)

    print(p1.phone1())