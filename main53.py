c = input("quyidagilardan birini tanlang:  1, 2, 3, 4, 5:  ")
lugat = {
    "O'zbekiston1":{
        "poytaxt": "Toshkent",
        "eng katta shahar": "Toshkent"
    },
    "O'zbekiston2":{
        "rasmiy til/": "o'zb, qor",
    },
    "O'zbekiston3":{
        "Prezident": "Sh Mirziyoyev",
        "Senat raisi": "Tanzilla Norboyeva"
        },
    "O'zbekiston4":{
        "maydoni": "448978kmkv",
        "o'rni": "56"
    },
    "O'zbekiston5": {
        "aholi": "35603443",
        "o'rni": "42"
    }
    }
if c == "1":
    print(lugat["O'zbekiston1"])
elif c == "2":
    print(lugat["O'zbekiston2"])
elif c == "3":
    print(lugat["O'zbekiston3"])
elif c == "4":
    print(lugat["O'zbekiston4"])
elif c == "5":
    print(lugat["O'zbekiston5"])