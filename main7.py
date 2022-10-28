a = [["ism1", "ism2", "ism3,"], ["familiya1", "familiya2", "familiya3"], ["yosh1", "yosh2", "yosh3"]]
b = input("sonni kiriting: ")

if b == "1":
    print(a[0][0], a[1][0], a[2][0])
elif b == "2":
    print(a[0][1], a[1][1], a[2][1])
elif b == "3":
    print(a[0][2], a[1][2], a[2][2])
else:
    print("siz dasturga kirdingiz")

