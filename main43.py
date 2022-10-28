a = int(input("sonlardan birini tanlang: 1- kalkulyator, 2-listlar, 3-gul haqida ma'lumot, 4 - taxminiy sonlar orasidagi sonlar yig'indisini topish,"))

if a == 1:
    q = input("ismingizni kiriting: ")
    w = input("familiyangizni kiriting: ")
    parol = int(input("parolingizni kiriting: "))
    r = int(input("1-sonni kiriting: "))
    t = int(input("2-sonni kiriting: "))
    amal = input("amal kiriting: ")
    def kalkulyator(r, t):
        if amal == "-":
            print(r - t)
        elif amal == "+":
            print(r + t)
        elif amal == "/":
            print(r / t)
        elif amal == "*":
            print(r * t)
    kalkulyator(r, t)

elif a == 2:
    y = [[1], [2], [3], [4], ["qw", "rt", "io", ["pa"]]]
    u = input("quyidagilardan birini tanlang:    sonlar,   harflar;  ")
    if u == "sonlar":
        print(y[0], y[1], y[2], y[3])
    elif u == "harflar":
        print(y[4][0], y[4][1], y[4][2], y[4][3][0])

elif a == 3:
    class Gul:
        def __init__ (self, nomi, hidi, rangi, bargi):
            self.nomi = nomi
            self.hidi = hidi
            self.rangi = rangi
            self.bargi = bargi
    g = Gul("nomi atirgul, ", "hidi yaxshi, ", "rangi qizil, ", "bargi yashil ")
    print(g.nomi, g.hidi, g.rangi, g.bargi)

elif a == 4:
    i = int(input("1-sonni kiriting: "))
    o = int(input("2-sonni kiriting: "))
    p = 0
    for x in range(i, o):
        p += x
        print(p)