from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

print("Uydu Hareket Simülasyonu")

#Baslangic sartlari

#Ilk konum [m]
x0 = 10000000
y0 = 20000000
z0 = 23000000
r0 = [32078029.86]   #Bileske Konumu

#Ilk hiz [m/s]
U0 = 5000   #Uzunlamasina Hiz [m/s]
V0 = 5000   #Yanlamasina Hiz [m/s]
W0 = 3500   #Dikey Hiz [m/s]
S0 = [7889.866919]    ##Bileske Hizi

#Ilk zaman [s]
t=0

#Kepler Sabiti
yy = 6.67*(10**(-11))   # [(m**3)/(kg*(m**2))]

#Dunyanin Kutlesi
M = 5.976*(10**(24))    # [kg]

# r Uydunun kutle merkezi ile dunyanin kutle merkezi arasindaki mesafedir [m]

#x, y, z uydunun kartezyen koordinatlaridir [m]

print("t ={}[sn]  and  x({})={}[m]  and  U=({})={}[m/s**2]".format(t, t, x0, t, U0))
print("t ={}[sn]  and  y({})={}[m]  and  V=({})={}[m/s**2]".format(t, t, y0, t, V0))
print("t ={}[sn]  and  z({})={}[m]  and  W=({})={}[m/s**2]".format(t, t, z0, t, W0))

while t <= 3 :
    t+= 1
    x0 = x0 + t * U0
    y0 = y0 + t * V0
    z0 = z0 + t * W0
    r0 = sqrt ((x0 ** (2)) + (y0 ** (2)) + (z0 ** (2)))
    U0 = U0 - t * yy * M * (x0 / (r0 ** 3))
    V0 = V0 - t * yy * M * (y0 / (r0 ** 3))
    W0 = W0 - t * yy * M * (z0 / (r0 ** 3))
    S0 = sqrt ((U0 ** (2)) + (V0 ** (2)) + (W0 ** (2)))
    print("t ={}[sn]  and  r({})={}[m]  and  S=({})={}[m/s**2]".format(t, t, r0, t, S0))

