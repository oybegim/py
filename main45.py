class Hayvon:
    def __init__(self, ismi, yoshi):
        self.ismi = ismi
        self.yoshi = yoshi
    def __str__(self):
        return f"{self.ismi} {self.yoshi}"

class Ot(Hayvon):
    def __init__(self, ismi, yoshi, kgsi):
        super().__init__(ismi, yoshi)
        self.kgsi = kgsi
    def ot1(self):
        print(self.ismi, self.yoshi, self.kgsi)
o1 = Ot("qwe", 1, 2)
o2 = Ot("rty", 2, 3)
o3 = Ot("tyu", 3, 4)


class Maymun(Hayvon):
    def __init__(self, ismi, yoshi, laqabi):
        super().__init__(ismi, yoshi)
        self.laqabi = laqabi
    def maymun1(self):
        print(self.ismi, self.yoshi, self.laqabi)
m1 = Maymun("yui", 4, 5)
m2 = Maymun("uio", 5, 6)
m3 = Maymun("iop", 6, 7)


class Sher(Hayvon):
    def __init__(self, ismi, yoshi, rangi):
        super().__init__(ismi, yoshi)
        self.rangi = rangi
    def sher1(self):
        print(self.ismi, self.yoshi, self.rangi)
s1 = Sher("asd", 7, "sdf")
s2 = Sher("dfg", 8, "fgh")
s3 = Sher("ghj", 9, "hjk")



print(s3.sher1())
