from math import sqrt
import matplotlib.pyplot as plt


print("Uydu Hareket Simülasyonu")


A0 = float(input("x0 Konum Degerini Giriniz:"))
B0 = float(input("y0 Konum Degerini Giriniz:"))
C0 = float(input("z0 Konum Degerini Giriniz:"))
D0 = float(input("U0 Hiz Degerini Giriniz:"))
E0 = float(input("V0 Hiz Degerini Giriniz:"))
F0 = float(input("W0 Hiz Degerini Giriniz:"))


def baslangicSartlarinaDon():       # baslangicSartlarinaDon() komutu ile baslangic sartlarina doner
    # Parametreleri ilk degerlerine donduren fonksiyon

    # Ilk konum [m]
    #Bu degerler standart GPS uydusu degerleridir
    #Ilk konumlari
    #x0 = 10000000
    #y0 = 20000000
    #z0 = 23000000
    #r0 = 32078029.86   #Bileske Konumu
    x0 = A0
    y0 = B0
    z0 = C0
    r0 = sqrt((x0 ** (2)) + (y0 ** (2)) + (z0 ** (2)))

    # Ilk hiz [m/s]
    #U0 = 5000  # Uzunlamasina Hiz [m/s]
    #V0 = 5000  # Yanlamasina Hiz [m/s]
    #W0 = 3500  # Dikey Hiz [m/s]
    # S0 = [7889.866919]    ##Bileske Hizi
    #S0 = 7889.866919
    U0 = D0
    V0 = E0
    W0 = F0
    S0 = sqrt((U0 ** (2)) + (V0 ** (2)) + (W0 ** (2)))

    # Ilk zaman [s]

    # Kepler Sabiti
    yy = 6.67 * (10 ** (-11))  # [(m**3)/(kg*(m**2))]

    # Dunyanin Kutlesi
    M = 5.976 * (10 ** (24))  # [kg]

    #r Uydunun kutle merkezi ile dunyanin kutle merkezi arasindaki mesafedir [m]
    # x, y, z uydunun kartezyen koordinatlaridir [m]

    return x0, y0, z0, r0, U0, V0, W0, S0, yy, M


# Grafik icin liste olusturdum.
# B = list()  #Zaman listesi
# C = list()  #r0 listesi
# D = list()  #S0 listesi
x0, y0, z0, r0, U0, V0, W0, S0, yy, M = baslangicSartlarinaDon()
B1 = [0]
C1 = [r0]
D1 = [S0]


# DeltaT=0.1 ve 100000 adim icin
deltaT = 0.1
for t in range(1, 100000):
    B1.append(t * deltaT)
    x0 = x0 + deltaT * U0
    y0 = y0 + deltaT * V0
    z0 = z0 + deltaT * W0
    r0 = sqrt((x0 ** (2)) + (y0 ** (2)) + (z0 ** (2)))
    C1.append(r0)
    U0 = U0 - deltaT * yy * M * (x0 / (r0 ** 3))
    V0 = V0 - deltaT * yy * M * (y0 / (r0 ** 3))
    W0 = W0 - deltaT * yy * M * (z0 / (r0 ** 3))
    S0 = sqrt((U0 ** (2)) + (V0 ** (2)) + (W0 ** (2)))
    D1.append(S0)


x0, y0, z0, r0, U0, V0, W0, S0, yy, M = baslangicSartlarinaDon()
B2 = [0]
C2 = [r0]
D2 = [S0]


# DeltaT=1 ve 10000 adim icin
deltaT = 1
for t in range(1, 10000):
    B2.append(t * deltaT)
    x0 = x0 + deltaT * U0
    y0 = y0 + deltaT * V0
    z0 = z0 + deltaT * W0
    r0 = sqrt((x0 ** (2)) + (y0 ** (2)) + (z0 ** (2)))
    C2.append(r0)
    U0 = U0 - deltaT * yy * M * (x0 / (r0 ** 3))
    V0 = V0 - deltaT * yy * M * (y0 / (r0 ** 3))
    W0 = W0 - deltaT * yy * M * (z0 / (r0 ** 3))
    S0 = sqrt((U0 ** (2)) + (V0 ** (2)) + (W0 ** (2)))
    D2.append(S0)


def grafik1():
    # DeltaT=0.1 ve 100000 adim icin olusturulan grafik
    plt.plot(B1, C1)
    plt.title("DeltaT=0.1 ve 100000 adim icin Zaman Konum Grafigi")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g11.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()
    plt.plot(B1, D1)
    plt.title("DeltaT=0.1 ve 100000 adim icin Zaman Hiz Grafigi")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Hiz [m/s]")
    plt.savefig(fname="g12.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()


def grafik2():
    # DeltaT=1 ve 10000 adim icin olusturulan grafik
    plt.plot(B2, C2)
    plt.title("DeltaT=1 ve 10000 adim icin Zaman Konum Grafigi")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g21.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()
    plt.plot(B2, D2)
    plt.title("DeltaT=1 ve 10000 adim icin Zaman Hiz Grafigi")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Hiz [m/s]")
    plt.savefig(fname="g22.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()


grafik1()
grafik2()
