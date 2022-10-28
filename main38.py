class Gul:
    def __init__(self, nomi, hidi, yoshi, bargi):
        self.nomi = nomi
        self.hidi = hidi
        self.yoshi = yoshi
        self.bargi = bargi
g1 = Gul("ymso", "yaxshi", 777, 77)
print(g1.nomi, g1.hidi, g1.yoshi, g1.bargi)

class Odam:
    def __init__(self, ismi, familiyasi, yoshi, rangi):
        self.ismi = ismi
        self.familiyasi = familiyasi
        self.yoshi = yoshi
        self.rangi = rangi
o1 = Odam("abc", "ABC", 77, "oq")
print(o1.ismi, o1.familiyasi, o1.yoshi, o1.yoshi)

class Tg:
    def __init__(self, kanal, guruh, shaxsiy, bot):
        self.kanal = kanal
        self.guruh = guruh
        self.shaxsiy = shaxsiy
        self.bot = bot
t1 = Tg("abc", "ABC", "qwe", "QWE")
print(t1.kanal, t1.guruh, t1.shaxsiy, t1.bot)

class Maktab:
    def __init__(self, nomi, maydoni, qavati, bnsi):
        self.nomi = nomi
        self.maydoni = maydoni
        self.qavati = qavati
        self.bnsi = bnsi
m1 = Maktab("qwe", "QWER", 7, 777)
print(m1.nomi, m1.maydoni, m1.qavati, m1.bnsi)

a = int(input("sonlardan birini tanlang: 1, 2, 3, 4"))

if a == "1":
    print(g1.nomi, g1.hidi, g1.yoshi, g1.bargi)
elif a == "2":
    print(o1.ismi, o1.familiyasi, o1.yoshi, o1.yoshi)  
elif a == "3":
    print(t1.kanal, t1.guruh, t1.shaxsiy, t1.bot)
elif a == "4":
    print(m1.nomi, m1.maydoni, m1.qavati, m1.bnsi)
