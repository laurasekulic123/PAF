import prvi_zad as calc
import numpy as np
import matplotlib.pyplot as plt
import math



# Testiramo na kubnoj funkciji
f =  lambda x: x**3

x = np.linspace(0, 1, 100)
dfdx = 3*x**2  # Analitičko rješenje

# Numerička derivacija s dvostepenom formulom
x1 = calc
dfdx = calc

def f1(x):
    return x**3

def f2(x):
    return math.sin(x)

print(calc.derivacija(f1,x))
print(calc.derivacija_na_rasponu(f2,1,2,100))


print(x1)
print(dfdx)


def f(x):
    return x

num_dn,num_up = calc.integral_up_dn(f,0,1,2)
print('donja meda: {0:}  \n gornja meda: {1:}'.format(num_dn,num_up))


plt.plot(num_dn)
plt.plot(num_up)
plt.show()
