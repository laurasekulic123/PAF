import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Pitajte korisnika za početnu brzinu i kut otklona
v0 = float(input("Unesite početnu brzinu u m/s: "))
theta = float(input("Unesite kut otklona u stupnjevima: "))

# Pretvorite kut otklona u radijane
theta = np.radians(theta)

# Definirajte funkciju koja će riješiti diferencijalne jednadžbe
def projectile_motion(state, t):
    x, y, vx, vy = state
    ax = 0
    ay = -9.81
    return [vx, vy, ax, ay]

# Definirajte početne uvjete
x0 = 0
y0 = 0
vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)
state0 = [x0, y0, vx0, vy0]

# Izvršite numeričko rješavanje funkcije za vremenski interval od 0 do 10 sekundi
t = np.linspace(0, 10, 101)
states = odeint(projectile_motion, state0, t)

# Izračunajte x i y pozicije tijekom vremena i spremite ih u nizove
x = states[:, 0]
y = states[:, 1]

# Nacrtajte grafove
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.plot(x, y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("x-y graf")

plt.subplot(1, 3, 2)