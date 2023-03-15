import matplotlib.pyplot as plt
import numpy as np
def nacrtaj_funkciju(x1,y1,x2,y2):
    x1=float(input('unesite x1: '))
    y1=float(input('upisite y1: '))
    x2=float(input('upisite x2: '))
    y2=float(input('upisite y2: '))

    k=(y2-y1)/(x2-x1)
    l=y1-(k*x1)
    print('y={}x+{}'.format(k,l))
    z=np.linspace(0,10,1000)
    x=[x1,x2]
    y=[y1,y2]
    plt.plot(x,y)
    plt.show()
    im.save(zadatak_5.png)