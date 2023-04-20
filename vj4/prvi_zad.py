import math
import matplotlib.pyplot as plt
import numpy as np

class cestica:
    g=9.81

    def __init__(self,pocetna_brzina,x0,y0,theta,dt=0.01):


        self.pocetna_brzina= pocetna_brzina
        self.theta = theta
        self.x0=x0
        self.y0=y0
        self.dt=dt
        self.x= []
        self.y = []



    def reset(self):
        self.pocetna_brzina = 0
        self.theta = 0
        self.v0 = 0
        self.x0 = 0
        self.y.clear()
        self.x.clear()


    def range(self):
        
        g= 9.81
        t= 0
        theta_r= (self.theta / 180)*np.pi
        vx0= self.pocetna_brzina * np.cos(theta_r)
        vy= self.pocetna_brzina * np.sin(theta_r)

        while self.y0 >= 0:

            self.x0 = self.x0 + vx0 * self.dt
            self.x.append(self.x0)

            self.y0 = self.y0 + vy * self.dt
            self.y.append(self.y0)

            vy = vy - g * self.dt

            t += self.dt

        return self.x[-1]
        self.y0 = 0
     


    def __move(self, F, m ,t):
        t0 = 0
        g= 9.81
        dt=0.01

        theta_r = (self.theta / 180) + np.pi
        vx0= self.v0 * np.cos(theta_r)
        vy0= self.v0 * np.sin(theta_r)

        while t0 < t:
            self.x0=self.x0 + vx0*dt
            self.x.append(self.x0)
            vy = vy0 - g* dt
            vy0 = vy



    
    def plot_trajectory(self):
        plt.plot(self.x,self.y)
        plt.show()


    def analiticki(self):
        domet= ((self.pocetna_brzina)**2 * np.sin(2*((self.theta / 180)*np.pi))) / 9.81
        return domet
    


