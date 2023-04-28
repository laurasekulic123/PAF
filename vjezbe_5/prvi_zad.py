import numpy as np
import math


def derivacija(f, x, eps=1e-6, metoda='three-step'):
    
    if metoda == 'two-step':
        return (f(x+eps) - f(x-eps)) / (2*eps)
    elif metoda == 'three-step':
        return (-f(x+2*eps) + 4*f(x+eps) - 3*f(x)) / (2*eps)
   
def derivacija_na_rasponu(f, a, b, N, eps=1e-6, metoda='three-step'):
   
    x = np.linspace(a, b, N)
    dfdx = np.zeros(N)
    for i in range(N):
        dfdx[i] = derivacija(f, x[i], eps=eps, metoda=metoda)
    return x, dfdx



def integral_up_dn(funk, dn , up, N):
    sum_up= 0
    sum_dn= 0
    dx= abs(up-dn)/N
    for i in range(0,N):
        sum_dn= funk(i*dx)*dx
        sum_up= funk((i+dx)*dx)*dx
        print((i+1)*dx,funk((i+1)*dx))
    return sum_dn , sum_up

