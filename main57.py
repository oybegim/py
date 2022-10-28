import time
try:
    a = int(input("parol kiriting"))
    b = input("login kiriting")
    c = 0
    if a == 1234 and b == "so":
        print("siz dasturdasiz")
    elif a != 1234 and b == "so":
        while c <2:
            c += 1
            time.sleep(2)
            print(c)
    
    
    elif a != 1234 and b != "so":
        while c <3:
            c += 1
            time.sleep(3)
            print(c)
        
except ValueError:
    print("siz str kiritdingiz")