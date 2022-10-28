ism = input("ismingizni kiriting: ")
fam = input("familiyangizni kiriting: ")
tel = input ("tel raqam kiriting: ")

if ism != "abc" and fam == "qwerty" and tel == "912345678":
    print("siz xato ism kiritdingiz")
elif ism == "abc" and fam != "qwerty" and tel == "912345678":
    print("siz xato familiya kiritdingiz")
elif ism == "abc" and fam == "qwerty" and tel != "912345678":
    print("siz xato tel nomer kiritdingiz")
else:
    print("siz dasturga kira olmadingiz")


