class Meva:
    def __init__(self, rangi, tami):
        self.rangi = rangi
        self.tami = tami
    def __str__(self):
        return f"{self.rangi} {self.tami}"
class Banan(Meva):
    def __init__(self, rangi, tami, kg):
        super().__init__(rangi, tami)
        self.kg = kg
    def banan1(self):
        print(self.rangi, self.tami, self.kg)
b1 = Banan("qwe", "wer", 1)
b2 = Banan("ert", "rty", 2)
b3 = Banan("tyu", "yui", 3)


class Shaftoli(Meva):
    def __init__(self, rangi, tami, donak):
        super().__init__(rangi, tami)
        self.donak = donak
    def shaftoli2(self):
        print(self.rangi, self.tami, self.donak)
sh1 = Shaftoli("uio", "iop", "asd")
sh2 = Shaftoli("sdf", "dfg", "fgh")
sh3 = Shaftoli("ghj", "hjk", "jkl")


class Olma(Meva):
    def __init__(self, rangi, tami, donakchasi):
        super().__init__(rangi, tami)
        self.donakchasi = donakchasi
    def olma3(self):
        print(self.rangi, self.tami, self.donakchasi)
o1 = Olma("klz", "zxc", 4)
o2 = Olma("xcv", "cvb", 5)
o3 = Olma("vbn", "bnm", 6)



print(o3.olma3())




