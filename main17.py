try:
    a = int(input("1-sonni kiriting: "))
    b = int(input("2-sonni kiriting: "))
    amal = input("amal kiriting: ")
    
    if amal == "+":
        print(a + b)
    elif amal == "-":
        print(a - b)
    elif amal == "*":
        print(a * b)
    elif amal == "/":
        print(a / b)
except:
    print()