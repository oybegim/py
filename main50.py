a = input("sizga qaysi kk: ")
c = input("a va b")
lugat = {
    "samsung": {
        "a": ["qwe", 1],
        "b": ["wer", 2]
    },
    "huawei": {
        "a": ["ert", 3],
        "b": ["rty", 4]
    },
    "apple": {
       "a": ["tyu", 5],
       "b": ["yui", 6]
}
}
b = a.lower()

if b.lower() =="Samsung".lower():
    print(lugat["samsung"])
    if c == "a":
        print(["qwe", 1])
    elif c == "b":
        print(["wer", 2])

elif b.lower() == "Huawei".lower():
    print(lugat["huawei"])
    
    if c == "a":
        print(["ert", 3])
    elif c == "b":
        print(["rty", 4])

elif "apple" == "Apple".lower():
    print(lugat["apple"])
    if c == "a":
        print(["tyu", 5])
    elif c == "b":
        print(["yui", 6])







