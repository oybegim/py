a = input("quyidagilardan birini tanlang:  1, 2, 3, 4, 5:  ")
lugat = {
    "Benom":{
        "music": ["Parcha"],
        "yili": ["2022"],
    },

    "Uzmir & Mira":{
        "music": ["Judolik"], 
        "vqti": ["3:17"],
    },

    "Hilola Samirazar":{
        "music": ["Elfida"],
        "tili": ["bilmayman"],
    },

    "Pouya Bayati": {
        "music": ["Tanhaii Naro"],
        "tili": ["tojikcha"]
    },

    "Oybek Sangin & Amin": {
        "music": ["Qoyib yubor"],
        "yili": ["premyera"]
    }
}

if a == "1":
    print(lugat["Benom"])
elif a == "2":
    print(lugat["Uzmir & Mira"])
elif a == "3":
    print(lugat["Hilola Samirazar"])
elif a == "4":
    print(lugat["Pouya Bayati"])
elif a == "5":
    print(lugat["Oybek Sangin & Amin"])
