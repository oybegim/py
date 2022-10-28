a = 1

try:
    print(b)
except NameError:
    print("xato")

try:
    a + "so"
except TypeError:
    print("sintaksis xato")

try:
    a + "7"
except TypeError:
    print("xatoo")

try:
    int("so")
except ValueError:
    print("bir nimala")
