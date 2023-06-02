import numpy as np
import matplotlib.pyplot as plt
import math

class Gravitacija:
    def __init__(self):
        self.x1 = []
        self.x2 = []
        self.y1 = []
        self.y2 = []

    def init(self, m1, m2, r1, r2, v1, v2, konstanta=6.67e-11, t0=0, dt=86400):
        self.t = t0
        self.M = m1
        self.m = m2
        self.R = np.array(r1)
        self.r = np.array(r2)
        self.V = np.array(v1)
        self.v = np.array(v2)
        self.G = konstanta
        self.dt = dt
        self.x1.append(self.R[0])
        self.y1.append(self.R[1])
        self.x2.append(self.r[0])
        self.y2.append(self.r[1])

    def move(self, T):
        while self.t < T:
            Rr = np.sqrt((self.R[0] - self.r[0]) ** 2 + (self.R[1] - self.r[1]) ** 2)
            rR = np.sqrt((self.r[0] - self.R[0]) ** 2 + (self.r[1] - self.R[1]) ** 2)
            A = -(self.G * self.m) / (Rr ** 3) * (self.R - self.r)
            a = -(self.G * self.M) / (rR ** 3) * (self.r - self.R)

            self.V = self.V + A * self.dt
            self.v = self.v + a * self.dt
            self.R = self.R + self.V * self.dt
            self.r = self.r + self.v * self.dt

            self.x1.append(self.R[0])
            self.x2.append(self.r[0])
            self.y1.append(self.R[1])
            self.y2.append(self.r[1])
            self.t += self.dt

        return self.x1, self.y1, self.x2, self.y2


# Inicijalizacija objekta klase Gravitacija
gravitacija = Gravitacija()

# Postavljanje početnih uvjeta
m1 = 1.989e30  # Masa Sunca [kg]
m2 = 5.9742e24  # Masa Zemlje [kg]
r1 = [0, 0]  # Početni položaj Sunca [m]
r2 = [1.486e11, 0]  # Početni položaj Zemlje [m]
v1 = [0, 0]  # Početna brzina Sunca [m/s]
v2 = [0, 29783]  # Početna brzina Zemlje [m/s]

gravitacija.init(m1, m2, r1, r2, v1, v2)

# Pokretanje simulacije
T = 365.242 * 24 * 60 * 60  # Jedna godina u sekundama
x1, y1, x2, y2 = gravitacija.move(T)

# Crtanje grafa
plt.figure(figsize=(8, 8))
plt.plot(x1, y1, label='Sunce')
plt.plot(x2, y2, label='Zemlja')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Putanja Sunca i Zemlje')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
