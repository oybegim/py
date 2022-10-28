class Odam:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya
    def __str__(self):
        return f"{self.ism} {self.familiya}"

class Bobo(Odam):
    def __init__(self, ism, familiya, yosh):
        super().__init__(ism, familiya)
        self.yosh = yosh
    def boboo(self):
        print(self.ism, self.familiya, self.yosh)
b1 = Bobo("abc", "ABC", 107)
b2 = Bobo("qwe", "QWE", 108)
b3 = Bobo("wer", "WER", 109)

class Buvi(Odam):
    def __init__(self, ism, familiya, rang):
        super().__init__(ism, familiya)
        self.rang = rang
    def buvii(self):
        print(self.ism, self.familiya, self.rang)
b4 = Buvi("rty", "RTY", "abc")
b5 = Buvi("tyu", "TYU", "Abc")
b6 = Buvi("yui", "YUi", "ABc")

class Ota(Odam):
    def __init__(self, ism, familiya, ochestva):
        super().__init__(ism, familiya)
        self.ochestva = ochestva
    def otaa(self):
        print(self.ism, self.familiya, self.ochestva)
o1 = Ota("uio", "UIO", "abc")
o2 = Ota("iop", "IOP", "ABC")
o3 = Ota("asd", "ASD", "ABC")

print(o3.otaa())