try:
    a = int(input("1-sonni kiriting: "))
    b = int(input("2-sonni kiriting: "))
    amal = input("amalni kiriting: ")
    if amal == "-":
        print(a - b)
    elif amal == "+":
        print(a + b)
    elif amal == "*":
        print(a * b)
    elif amal == "/":
        print(a / b)
except ZeroDivisionError:
    print("sonni nolga bo'lib bo'lmaydi")
except:
    print("son bilan tekstda amal bajarib bo'lmaydi")

    