try:

    a = int(input("1-sonni kiriting: "))
    b = int(input("2-sonni kirirting: "))
    amal = input("amalni kiriting: ")

    if amal == "+":
        print(a + b)
    elif amal == "-":
        print(a - b)
    elif amal == "*":
        print(a * b)
    elif amal == "/":
        print(a / b)

except ZeroDivisionError:
    print("sonni 0 ga bo'lib bo'lmaydi")
except ValueError:
    print("son va tekstda amal bajarib bo'lmaydi")
except:
    print("sizda qandaydir xatolik bor")





