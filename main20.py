


class Gul:
    def __init__(self, ismi, hidi, ogirligi):
        self.ismi = ismi 
        self.hidi = hidi
        self.ogirligi = ogirligi
    def __str__(self): 
        return f"Ism: {self.hidi}, Hidi: {self.hidi}, Ogirligi: {self.ogirligi}"
g1 = Gul("atirgul", "shirin", 1 )
g2 = Gul("atirgul2", "shirin2", 2 )
g3 = Gul("atirgul3", "shirin3", 3 )
print(g1)
print(g2)
print(g3)

class Hayvon:
    def __init__(self, turi, yoshi, ogirligi):
        self.turi = turi
        self.yoshi = yoshi
        self.ogirligi = ogirligi
    def __str__(self):
        return f"Turi: {self.turi}, Yoshi: {self.yoshi}, ogirligi: {self.ogirligi}"
h1 = Hayvon("qwe", 1, 2)
h2 = Hayvon("wer", 2, 3)
h3 = Hayvon("ert", 3, 4)
print(h1)
print(h2)
print(h3)

class Maktab:
    def __init__(self, nomi, maydoni, qavati):
        self.nomi = nomi
        self.maydoni = maydoni
        self.qavati = qavati
    def __str__(self):
        return f"Nomi: {self.nomi}, Maydoni: {self.maydoni}, Qavati: {self.qavati}"
m1 = Maktab("rty", 1, 2 )
m2 = Maktab("tyu", 2, 3 )
m3 = Maktab("yui", 3, 4 )
print(m1)
print(m2)
print(m3)

class Choco:
    def __init__(self, nomi, kattaligi, mazasi):
        self.nomi = nomi
        self.kattaligi = kattaligi
        self.mazasi = mazasi
    def __str__(self):
        return f"Nomi: {self.nomi}, Kattaligi: {self.kattaligi}, Mazasi: {self.mazasi}"

c1 = Choco("uio", 2, "yaxshi")
c2 = Choco("iop", 3, "yamon")
c3 = Choco("ops", 5, "norm")
print(c1)
print(c2)
print(c3)

class Deraza:
    def __init__(self, nomi, uzunligi, sifati):
        self.nomi = nomi
        self.uzunligi = uzunligi
        self.sifati = sifati
    def __str__(self):
        return f"Nomi: {self.nomi}, Uzunligi: {self.uzunligi}, Sifati: {self.sifati}"
d1 = Deraza("asd", 4, "sdf")
d2 = Deraza("dfg", 5, "fgh")
d3 = Deraza("ghj", 6, "hjk")
print(d1)
print(d2)
print(d3)

class Komp:
    def __init__(self, win, core, aspire):
        self.win = win
        self.core = core
        self.aspire = aspire
    def __str__(self):
        return f"Win: {self.win}, Core: {self.core}, Aspire: {self.aspire}"
k1 = Komp(1, 2, 3)
k2 = Komp(2, 3, 4)
k3 = Komp(3, 4, 5)
print(k1)
print(k2)
print(k3)

class Tel:
    def __init__(self, prog, sifat, nom):
        self.prog = prog
        self.sifat = sifat
        self.nom = nom
    def __str__(self):
        return f"Prog: {self.prog}, Sifat: {self.sifat}, Nom: {self.nom}"
t1 = Tel("hjk", "jkl", "klz")
t2 = Tel("lzx", "zxc", "xcv")
t3 = Tel("cvb", "vbn", "bnm")
print(t1)
print(t2)
print(t3)

class Kafe:
    def __init__(self, gigen, joy, fastfood):
        self.gigen = gigen 
        self.joy = joy
        self.fastfood = fastfood
    def __str__(self):
        return f"Gigen: {self.gigen}, Joy: {self.joy}, Fastfood: {self.fastfood}"
k4 = Kafe("qwe", "wer", "ert")
k5 = Kafe("tyu", "yui", "iop")
k6 = Kafe("asd", "sdf", "dfg")
print(k4)
print(k5)
print(k6)

class Uy:
    def __init__(self, joy, katta, qulay):
        self.joy = joy
        self.katta = katta
        self.qulay = qulay
    def __str__(self):
        return f"Joy: {self.joy}, Katta: {self.katta}, Qulay: {self.qulay}"
u1 = Uy("qw", "we", "rt")
u2 = Uy("ty","yu", "ui")
u3 = Uy("io", "po", "pa")
print(u1)
print(u2)
print(u3)

class Kitob:
    def __init__(self, sifat, katta, mano ):
        self.sifat = sifat
        self.katta = katta
        self.mano = mano
    def __str__(self):
        return f"Sifat: {self.sifat}, Katta: {self.katta}, Mano: {self.mano}"
K6 = Kitob("fg", "gh", "hj")
K7 = Kitob("kl", "lz", "zx")
K8 = Kitob("cv", "vb", "bn")
print(K6)
print(K7)
print(K8)