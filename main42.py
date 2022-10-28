a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = 0
if b % 2 ==1:
    print("b son toq son")
elif b % 2 != 1:
    print("b son juft son")
for x in range(a, b):
    c += x
    print(c)
    if c % 2 ==1:
        print("c toq son")
    elif c % 2 != 1:
        print("c juft son")