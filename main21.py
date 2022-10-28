class Odam:
    def __int__(self, ismi, familiyasi, yoshi):
        self.ismi = ismi 
        self.familiyasi = familiyasi
        self.yoshi = yoshi
    def __str__(self):
        return f"ism: {self.ismi}, Familiya: {self.familiyasi}, Yosh: {self.yoshi}" 

o1 = Odam("ab", "ABC", 1)
o2 = Odam("abc", "ABC", 2)
print(o1)
print(o2)
    
class Hayvon:
    def __int__(self, turi, laqabi, rangi):
        self.turi = turi
        self.laqabi = laqabi
        self.rangi = rangi
    def __str__(self):
        return f"Tur: {self.turi}, Laqab: {self.laqabi}, rang: {self.rangi}"
        
h1 = Hayvon("bcd", "BCD", 3)
h2 = Hayvon("bcd", "BCD", 4)
print(h1)
print(h2)
    
a = int(input("sonni tanlang: "))
if a == 1:
    print(o1)
    print(o2)
elif a == 2:
    print(h2)
    print(h2)