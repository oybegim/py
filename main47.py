class Dori:
    def __init__(self, tasiri, tami):
        self.tasiri = tasiri
        self.tami = tami
    def __str__(self):
        return f"{self.tasiri} {self.tami}"

class Lizak(Dori):
    def __init__(self,tasiri, tami, malumot):
        super().__init__(tasiri, tami)
        self.malumot = malumot
    def lizak1(self):
        print(self.tasiri, self.tami, self.malumot)
l1 = Lizak("qwe", "wer", "ert")
l2 = Lizak("rty", "tyu", "yui")
l3 = Lizak("uio", "iop", "asd")


class Anzibel(Dori):
    def __init__(self, tasiri, tami, bn1):
        super().__init__(tasiri, tami)
        self.bn1 = bn1
    def anzibel2(self):
        print(self.tasiri, self.tami, self.bn1)
a1 = Anzibel("sdf", "dfg", "fgh")
a2 = Anzibel("ghj", "hjk", "jkl")
a3 = Anzibel("klz", "lzx", "zxc")


class Sinepar(Dori):
    def __init__(self, tasiri, tami, bn2):
        super().__init__(tasiri, tami)
        self.bn2 = bn2
    def sinepar3(self):
        print(self.tasiri, self.tami, self.bn2)
s1 = Sinepar("xcv", "cvb", "vbn")
s2 = Sinepar("bnm", "nmq", "mqw")
s3 = Sinepar("ef", "rfg", "gr")


print(s3.sinepar3())








