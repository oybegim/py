a = int(input("birinchi sonni kiriting: "))
b = int(input("ikkinchi sonni kiriting: "))

def sanash(a, b):
    while a < b:
        b -= 1
        print(b)
        
sanash(a, b)