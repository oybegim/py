class Tel:
    def __init__(self, sms, igra):
        self.sms = sms
        self.igra = igra
    def __str__(self):
        return f"{self.sms} {self.igra}"
class Phone(Tel):
    def __init__(self, sms, igra, tg):
        super().__init__(sms, igra)
        self.tg = tg
    def phone1(self):
        print(self.sms, self.igra, self.tg)
p1 = Phone("qwe", "wer", "ert")
p2 = Phone("rty", "yui", "uio")
p3 = Phone("iop", "asd", "sdf")


class Iphone(Tel):
    def __init__(self, sms, igra, foto):
        super().__init__(sms, igra)
        self.foto = foto
    def iphone1(self):
        print(self.sms, self.igra, self.foto)
i1 = Iphone("dfg", "fgh", "ghj")
i2 = Iphone("hjk", "jkl", "klz")
i3 = Iphone("lzx", "zxc", "xcv")


class Android(Tel):
    def __init__(self, sms, igra, inst):
        super().__init__(sms, igra)
        self.inst = inst
    def android1(self):
        print(self.sms, self.igra, self.inst)
a1 = Android("cvb", "vbn", "bnm")
a2 = Android("qwe", "wer", "ert")
a3 = Android("rty", "tyu", "yui")


print(a1.android1())


