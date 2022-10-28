a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
amal = input("amalni kiriting: ")

def kalkulyator(a, b):
    if amal == "+":
        print(a + b)
    elif amal == "-":
        print(a - b)
    elif amal == "*":
        print(a * b)
    elif amal == "/":
        print(a / b)

kalkulyator(a, b)

