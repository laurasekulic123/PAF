##Napišite program u kojem korisnik definira iznos početne brzine v0 u
##m s i kut otklona θ u stupnjevima. Neka
##program crta x − y, x − t i y − t graf za prvih 10 sekundi gibanja u dvije dimenzije. Diferencijalne jednadžbe
##rješavajte numerički. Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.

import matplotlib.pyplot as plt
import numpy as np

v0=float(input('unesite pocetnu brzinu: '))
kut=float(input('unesite kut otklona: '))

kut=np.radians(kut)

lista_vremena=[]
lista_brzina=[]
lista_akc=[]
lista_vremena=[]
lista_pomaka=[]
lista_pomakay=[]

t0=0
v=0
dt=0.01
x0=0
y0=0
v1x=0
x1=0
y1=0
v1y=0
ax=0
ay=0
g=9.81
t=0

while t<=10:
    ax=0
    ay=-9.81
    v1x=10*np.cos(kut) + ax*dt
    v1y=10*np.sin(kut) + ay*dt
    v=np.cos(kut)*v1x*np.sin(kut)*v1y
    y1=0 + v1y*dt
    x1=v*dt
    lista_vremena.append(t)
    lista_brzina.append(v)
    lista_pomaka.append(x1)
    lista_akc.append(ay)
    t = t + dt


plt.subplot(1,3,1)
plt.plot(lista_vremena,lista_pomaka)

plt.subplot(1,3,2)
plt.plot(lista_vremena,lista_brzina)

plt.subplot(1,3,3)
plt.plot(lista_vremena,lista_akc)
plt.show()


    



