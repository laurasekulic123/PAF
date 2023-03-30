import math
import matplotlib.pyplot as plt
import numpy as np

M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])   # ovo je y
fi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]) # ovo je x

arit_sr_M = sum(M) / len(M)
arit_sr_fi = sum(fi) / len(fi)

D = (arit_sr_M * arit_sr_fi) / (arit_sr_fi * arit_sr_fi)


lista_y = []

for i in fi:
    y = D* i
    lista_y.append(y)

pogreska=np.sqrt( (1/len(fi)) *( ( (arit_sr_M**2) / (arit_sr_fi)**2) -D**2) )

plt.title('D={} +/- {}'.format(D,pogreska))
plt.scatter(fi,M)
plt.plot(fi,lista_y)
plt.show()