w = int(input("Raqam/= birini tanlang:  1, 2, 3, 4, 5  "))
lugat = {
    "Turkiya1": {
        "poytaxt": ["Anqara"], 
        "rasmiy til/": ["turk"]
    },
    "Turkiya2":{
        "prezident": ["Rajab Tayyip Erdo'g'on"],
        "pul birligi": ["lira"]
    },
    "Turkiya3":{
        "mydon": ["783,562kmkv"],
        "o'rni": [37]
    },
    "Turkiya4": {
        "aholi": [80810525],
        "o'rni": [16]
    },
    "Turkiya5":{
        "tel": [90],
        "int": [".tr"]
    }
}
if w == 1:
    print(lugat["Turkiya1"])
elif w == 2:
    print(lugat["Turkiya2"])
elif w == 3:
    print(lugat["Turkiya3"])
elif w == 4:
    print(lugat["Turkiya4"])
elif w == 5:
    print(lugat["Turkiya5"])