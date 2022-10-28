a = [100, 200, 300, 400, 500]
b = input("sonni kiriting: ")

if b == "1":
    for x in range(a[0]):
        print(x)
elif b == "2":
    for x in range(a[1]):
        print(x)
elif b == "3":
    for x in range(a[2]):
        print(x)
elif b == "4":
    for x in range(a[3]):
        print(x)
elif b == "5":
    for x in range(a[4]):
        print(x)
else:
    print("siz xato kiritdingiz")



a = int(input("birinchi son: "))
b = int(input("ikkinchi son: "))
c = 0 
for x in range(a, b):
    c += x
    print(c)