q = int(input("Raqam/= birini tanlang: 1, 2, 3, 4, 5,  "))
lugat = {
    "Ozarbayjon1": {
        "Poytaxt": ["Boku"],
        "Tuman": [61]
    }, 
    "Ozarbayjon2": {
        "shahar": [65],
        "shaharcha": [122]
    },
    "Ozarbayjon3":{
        "maydon": ["86600kmkv"],
        "o'rni": [112]
    }, 
    "Ozarbayjon4": {
        "aholi": [10027874],
        "o'rni": [90]
    },
    "Ozarbayjon5":{
        "tel": [994],
        "int": [".az"]
    }
}
if q == 1:
    print(lugat["Ozarbayjon1"])
elif q == 2:
    print(lugat["Ozarbayjon2"])
elif q == 3:
    print(lugat["Ozarbayjon3"])
elif q == 4:
    print(lugat["Ozarbayjon4"])
elif q == 5:
    print(lugat["Ozarbayjon5"])