a = input("qaysi qo'shiqchini tanlaysiz  Billie,  Sting:   ")


c = [[ "Onam", "Tanhoii Naro", ["gghggg"]], ["Zehir Gibi", "Hep Mi Ben", ["drdft"]]]


if a == "Billie":
    print(c[0])
elif a == "Sting":
    print(c[1]) 

b = int(input("listdagi tartib raqamni tanlang: "))
if b == 2:
    print(c[0][2])
    print(c[1][2])
