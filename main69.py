password = int(input("enter password"))
login = input("enter login")
if password == 1234:
    print("password is correct")
elif password != 1234:
    print("password is wrong")
elif login == "python1234":
    print("login is correct")
elif login != "python1234":
    print("login is wrong")
a = int(input("1 and 2"))
if a == 1:
    q = int(input("enter the first number"))
    w = int(input("enter the second number"))
    e = 0
    while q < w:
        q += 1
        e += q
        print(e)
elif a == 2:
    r = int(input("enter the first number"))
    t = int(input("enter the secod number"))
    y = 0
    for x in range (r, t):
        y += x
        print(y)
