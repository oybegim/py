b = int(input("quyidagilardan birini tanlang:  1, 2, 3, 4, 5:  "))
lugat = {
    "Anor":{
        "rangi": ["qizil"],
        "donasi": [3103]  
        },
    "Banan":{
        "rangi": ["sariq"],
        "donak": ["yoq"]
    },
    "Apelsin": {
        "rangi": ["olovrang"],
        "donak": ["bor"]
    },
    "Tarvuz":{
        "rangi": ["qizil"],
        "po'stlog'i": ["yashil"]
    },
    "Qovun":{
        "rangi": ["sariq"],
        "donak": ["yoq"]
    },
}
if b == 1:
    print(lugat["Anor"])
elif b == 2:
    print(lugat["Banan"])
elif b == 3:
    print(lugat["Apelsin"])
elif b == 4:
    print(lugat["Tarvuz"])
elif b == 5:
    print(lugat["Qovun"])
