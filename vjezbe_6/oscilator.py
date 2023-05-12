import numpy as np
import matplotlib.pyplot as plt


class HarmonicOscillator:
    def __init__(self, mass, k):
        self.mass = mass  
        self.k = k  
        
    def solve(self, x0, v0, dt, t):
        times = np.arange(0, t, dt)  
        
        x = np.zeros_like(times)  
        v = np.zeros_like(times)  
        a = np.zeros_like(times)  
        
    
        x[0] = x0
        v[0] = v0
        
        # Numeričko rješavanje 
        for i in range(1, len(times)):
            a[i-1] = -self.k / self.mass * x[i-1]  
            v[i] = v[i-1] + a[i-1] * dt  
            x[i] = x[i-1] + v[i] * dt  
        
        return times, x, v, a



if __name__ == '__main__':
    mass = 1.0
    k = 2.0
    x0 = 0.5
    v0 = 0.0
    dt = 0.01
    t = 10.0
    
    oscillator = HarmonicOscillator(mass, k)
    times, x, v, a = oscillator.solve(x0, v0, dt, t)
    
    
    plt.figure(figsize=(12, 8))
    
    #x-t
    plt.subplot(3, 1, 1)
    plt.plot(times, x)
    plt.xlabel('t')
    plt.ylabel('x')
    plt.title('x-t graf')
    
    #v-t
    plt.subplot(3, 1, 2)
    plt.plot(times, v)
    plt.xlabel('t')
    plt.ylabel('v')
    plt.title('v-t graf')
    
    #a-t
    plt.subplot(3, 1, 3)
    plt.plot(times, a)
    plt.xlabel('t')
    plt.ylabel('a')
    plt.title('a-t graf')
    
    plt.tight_layout()
    plt.show()

