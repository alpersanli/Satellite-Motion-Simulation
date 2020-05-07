from math import sqrt
import matplotlib.pyplot as plt
import random

print("Uydu Hareket Simülasyonu")
#Uydu hareket ölçüm simülasyonu.pdf dosyasi uzerine islendi

Q = 35000000    #r
W = 10000000    #x
E = 20000000    #y
R = sqrt((Q ** (2)) - (W ** (2)) - (E ** (2)))   #z
T = 3070    #S
Y = 1000    #U
U = 1000    #V
I = sqrt((T ** (2)) - (Y ** (2)) - (U ** (2)))   #W


def baslangicSartlarinaDon():       # baslangicSartlarinaDon() komutu ile baslangic sartlarina doner
    # Parametreleri ilk degerlerine donduren fonksiyon

    x0 = W
    y0 = E
    z0 = R
    r0 = Q

    U0 = Y
    V0 = U
    W0 = I
    S0 = T

    # Ilk zaman [s]

    # Kepler Sabiti
    yy = 6.67 * (10 ** (-11))  # [(m**3)/(kg*(m**2))]

    # Dunyanin Kutlesi
    M = 5.976 * (10 ** (24))  # [kg]

    #r Uydunun kutle merkezi ile dunyanin kutle merkezi arasindaki mesafedir [m]
    # x, y, z uydunun kartezyen koordinatlaridir [m]

    Gamax = 10  # Sonradan random ile eklenen, disaridan gelen bilgiler
    Gamay = 10
    Gamaz = 15
    Gamau = 0.02
    Gamav = 0.02
    Gamaw = 0.02

    return x0, y0, z0, r0, U0, V0, W0, S0, yy, M, Gamax, Gamay, Gamaz, Gamau, Gamav, Gamaw


# Grafik icin liste olusturdum.
# B = list()  #Zaman listesi gibi...

x0, y0, z0, r0, U0, V0, W0, S0, yy, M, Gamax, Gamay, Gamaz, Gamau, Gamav, Gamaw = baslangicSartlarinaDon()
B1 = [0]    #Zaman listesi
C1 = [r0]   #Bileske Konum Listesi
D1 = [S0]   #Bileske Hiz Listesi
N1 = [x0]   #x0 Listesi
P1 = [y0]   #y0 Listesi
E1 = [z0]   #z0 Listesi
Q1 = [U0]   #U0 Listesi
X1 = [V0]   #V0 Listesi
F1 = [W0]   #W0 Listesi
G1 = [x0]   #Zx Listesi
H1 = [y0]   #Zy Listesi
J1 = [z0]   #Zz Listesi
K1 = [U0]   #Zu Listesi
L1 = [V0]   #Zv Listesi
M1 = [W0]   #Zw Listesi

# DeltaT=0.1 ve 100000 adim icin
deltaT = 0.1
for t in range(1, 100000):
    B1.append(t * deltaT)
    Zx = x0 + Gamax * random.random()
    Zy = y0 + Gamay * random.random()
    Zz = z0 + Gamaz * random.random()
    x0 = x0 + deltaT * U0
    y0 = y0 + deltaT * V0
    z0 = z0 + deltaT * W0
    r0 = sqrt((x0 ** (2)) + (y0 ** (2)) + (z0 ** (2)))
    N1.append(x0)
    P1.append(y0)
    E1.append(z0)
    C1.append(r0)
    G1.append(Zx)
    H1.append(Zy)
    J1.append(Zz)

    Zu = U0 + Gamau * random.random()
    Zv = V0 + Gamav * random.random()
    Zw = W0 + Gamaw * random.random()
    U0 = U0 - deltaT * yy * M * (x0 / (r0 ** 3))
    V0 = V0 - deltaT * yy * M * (y0 / (r0 ** 3))
    W0 = W0 - deltaT * yy * M * (z0 / (r0 ** 3))
    S0 = sqrt((U0 ** (2)) + (V0 ** (2)) + (W0 ** (2)))
    Q1.append(U0)
    X1.append(V0)
    F1.append(W0)
    D1.append(S0)
    K1.append(Zu)
    L1.append(Zv)
    M1.append(Zw)


x0, y0, z0, r0, U0, V0, W0, S0, yy, M, Gamax, Gamay, Gamaz, Gamau, Gamav, Gamaw= baslangicSartlarinaDon()
B2 = [0]    #Zaman listesi
C2 = [r0]   #Bileske Konum Listesi
D2 = [S0]   #Bileske Hiz Listesi
N2 = [x0]   #x0 Listesi
P2 = [y0]   #y0 Listesi
E2 = [z0]   #z0 Listesi
Q2 = [U0]   #U0 Listesi
X2 = [V0]   #V0 Listesi
F2 = [W0]   #W0 Listesi
G2 = [x0]   #Zx Listesi
H2 = [y0]   #Zy Listesi
J2 = [z0]   #Zz Listesi
K2 = [U0]   #Zu Listesi
L2 = [V0]   #Zv Listesi
M2 = [W0]   #Zw Listesi


# DeltaT=1 ve 10000 adim icin
deltaT = 1
for t in range(1, 10000):
    B2.append(t * deltaT)
    Zx = x0 + Gamax * random.random()
    Zy = y0 + Gamay * random.random()
    Zz = z0 + Gamaz * random.random()
    x0 = x0 + deltaT * U0
    y0 = y0 + deltaT * V0
    z0 = z0 + deltaT * W0
    r0 = sqrt((x0 ** (2)) + (y0 ** (2)) + (z0 ** (2)))
    N2.append(x0)
    P2.append(y0)
    E2.append(z0)
    C2.append(r0)
    G2.append(Zx)
    H2.append(Zy)
    J2.append(Zz)

    Zu = U0 + Gamau * random.random()
    Zv = V0 + Gamav * random.random()
    Zw = W0 + Gamaw * random.random()
    U0 = U0 - deltaT * yy * M * (x0 / (r0 ** 3))
    V0 = V0 - deltaT * yy * M * (y0 / (r0 ** 3))
    W0 = W0 - deltaT * yy * M * (z0 / (r0 ** 3))
    S0 = sqrt((U0 ** (2)) + (V0 ** (2)) + (W0 ** (2)))
    Q2.append(U0)
    X2.append(V0)
    F2.append(W0)
    D2.append(S0)
    K2.append(Zu)
    L2.append(Zv)
    M2.append(Zw)


def grafik1():
    # x ve Zx / y ve Zy / z  ve  Zz / U  ve Zu / V ve Zv / W ve Zw   DeltaT=0.1 ve 100000 adim icin olusturulan grafikler
    plt.plot(B1, N1,'r', B1, G1, 'b')
    plt.title("x0 (Kirmizi) - Zx (Mavi) Grafigi DeltaT=0.1 ve 100000 adim icin")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g1.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()

    plt.plot(B1, P1,'r', B1, H1, 'b')
    plt.title("y0 (Kirmizi) - Zy (Mavi) Grafigi DeltaT=0.1 ve 100000 adim icin")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g2.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()

    plt.plot(B1, E1, 'r', B1, J1, 'b')
    plt.title("z0 (Kirmizi) - Zz (Mavi) Grafigi DeltaT=0.1 ve 100000 adim icin")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g3.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()

    plt.plot(B1, Q1, 'r', B1, K1, 'b')
    plt.title("U0 (Kirmizi) - Zu (Mavi) Grafigi DeltaT=0.1 ve 100000 adim icin")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g4.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()

    plt.plot(B1, X1, 'r', B1, L1, 'b')
    plt.title("V0 (Kirmizi) - Zv (Mavi) Grafigi DeltaT=0.1 ve 100000 adim icin")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g5.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()

    plt.plot(B1, F1, 'r', B1, M1, 'b')
    plt.title("W0 (Kirmizi) - Zw (Mavi) Grafigi DeltaT=0.1 ve 100000 adim icin")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g6.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()


def grafik2():
    # x ve Zx / y ve Zy / z  ve  Zz / U  ve Zu / V ve Zv / W ve Zw  DeltaT=1 ve 10000 adim icin olusturulan grafikler
    plt.plot(B2, N2,'r', B2, G2, 'b')
    plt.title("x0 (Kirmizi) - Zx (Mavi) Grafigi DeltaT=1 ve 10000 adim icin")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g7.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()

    plt.plot(B2, P2,'r', B2, H2, 'b')
    plt.title("y0 (Kirmizi) - Zy (Mavi) Grafigi DeltaT=1 ve 10000 adim icin")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g8.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()

    plt.plot(B2, E2, 'r', B2, J2, 'b')
    plt.title("z0 (Kirmizi) - Zz (Mavi) Grafigi DeltaT=1 ve 10000 adim icin")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g9.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()

    plt.plot(B2, Q2, 'r', B2, K2, 'b')
    plt.title("U0 (Kirmizi) - Zu (Mavi) Grafigi DeltaT=1 ve 10000 adim icin")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g10.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()

    plt.plot(B2, X2, 'r', B2, L2, 'b')
    plt.title("V0 (Kirmizi) - Zv (Mavi) Grafigi DeltaT=1 ve 10000 adim icin")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g11.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()

    plt.plot(B2, F2, 'r', B2, M2, 'b')
    plt.title("W0 (Kirmizi) - Zw (Mavi) Grafigi DeltaT=1 ve 10000 adim icin")
    plt.xlabel("Zaman [s]")
    plt.ylabel("Konum [m]")
    plt.savefig(fname="g12.png", facecolor="#f0f9e8", dpi=600, quality=95)
    plt.show()


grafik1()
grafik2()
