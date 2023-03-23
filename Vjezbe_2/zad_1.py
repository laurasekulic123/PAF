##Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg, a program crta x − t, v − t
##i a − t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji. Diferencijalne jednadžbe rješavajte
##numerički. Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.
import numpy as np
import matplotlib.pyplot as plt

N=float(input('unesite silu: '))
m=float(input('unesite masu: '))
lista_vremena=[]
lista_brzina=[]
lista_pomaka=[]
lista_akceleracije=[]
v=0.0
dt=0.01
x=0.0
t=0.0
a=float(N/m)
while t <= 10:
    v = v + a*dt
    x = x + v*dt
    lista_vremena.append(t)
    lista_brzina.append(v)
    lista_pomaka.append(x)
    lista_akceleracije.append(a)
    t=t+dt

plt.subplot(1,3,1)
plt.plot(lista_vremena,lista_brzina)

plt.subplot(1,3,2)
plt.plot(lista_vremena,lista_pomaka)

plt.subplot(1,3,3)
plt.plot(lista_vremena,lista_akceleracije)
plt.show()







