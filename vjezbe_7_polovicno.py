import numpy as np
import matplotlib.pyplot as plt

class particle:
    

    def __init__(self,mass,F,xn,yn,v,v0,vy,kut,dt=0.01,ro=1.22,A=0.001,Cd=1):

        self.mass =mass
        self.lista_y = []
        self.dt=dt
        self.ro=ro
        self.A= A
        self.Cd = Cd
        self.kut=kut
        self.x0= []
        self.y0= []
        self.v0= []
        self.a0= []
        self.F = F
        self.ax = []
        self.ay = []
        self.vx= []
        self.vy = []
        self.t = 0
        self.xn= xn
        self.yn = yn
        g=-9.81

  

    def gibanje(self,dt,T):      #T je cijeli period gibanja
        self.t= 0
        self.pozicije= []
        self.pozicije.append((0,0))
        
        while self.t <= T:
            self.pozicije.append(dt)
            self.t += dt

    def runge_kutta(self,dt,T):
        self.t= 0
        self.pozicije = []
        self.pozicije.append((0,0))

        while self.t <= T:
            self.pozicije.append(dt)
            self.t += dt

    def nova_pozicija(self,dt):

        g=9.81
        x ,y = self.pozicije[-1]
        axn= -(self.vx**2)*((self.ro*self.Cd*self.A)/2*self.mass)
        self.ax.append(axn)
        vxn1 = self.vx + axn*dt
        self.vx.append(vxn1)
        xn1 = self.xn + vxn1*dt
        self.x0.append(xn1)



        ayn=-g-((self.ro*self.Cd*self.A)/2*self.mass)
        self.ay.append(ayn)
        vyn1 = self.vy + ayn*dt
        self.vy.append(vyn1)
        yn1= self.yn + vyn1*dt
        self.y0.append(yn1)


    def __moveEuler(self):
        self.lista_y.append(self.lista_y[-1]+(self.vy[-1]*self.dt))
        self.vx.append(self.vx[-1]+(self.ax[-1]*self.dt))
        self.vy.append(self.vy[-1]+(self.ay[-1]*self.dt))
        self.ax.append((-1*self.vx[-1]/abs(self.vx[-1]))*(self.ro*self.Cd*self.A/(2*self.mass))*(self.vx[-1])**2)
        self.ay.append(-9.81-(self.vy[-1]/abs(self.vy[-1]))*(self.p*self.Cd*self.A/(2*self.mass))*(self.vy[-1])**2)
        self.ax.append(-1*np.sign(self.vx[-1])*(self.ro*self.Cd*self.A/(2*self.mass))*(self.vx[-1])**2)
        self.ay.append(-9.81-np.sign(self.vy[-1])*(self.ro*self.Cd*self.A/(2*self.mass))*(self.vy[-1])**2)



    def gibanje_runge_kutta(self,i):
         k_vx = [((-1*self.vx[-1]/abs(self.vx[-1]))*(self.ro*self.Cd*self.A/(2*self.mass))*(self.vx[-1])**2)*self.dt]
         k_vy = [(-9.81-(self.vy[-1]/abs(self.vy[-1]))*(self.ro*self.Cd*self.A/(2*self.mass))*(self.vy[-1])**2)*self.dt]
         k_vx = [(-1*np.sign(self.vx[-1])*(self.ro*self.Cd*self.A/(2*self.mass))*(self.vx[-1])**2)*self.dt]
         k_vy = [(-9.81-np.sign(self.vy[-1])*(self.ro*self.Cd*self.A/(2*self.mass))*(self.vy[-1])**2)*self.dt]
         k_x = [self.vx[-1]*self.dt]
         k_y = [self.vy[-1]*self.dt]
         
         
         for i in range(3):
            
            k_vx.append(((-1*(self.vx[-1]+0.5*k_vx[-1])/abs(self.vx[-1]+0.5*k_vx[-1]))*(self.ro*self.Cd*self.A/(2*self.mass))*(self.vx[-1]+0.5*k_vx[-1])**2)*self.dt)
            k_vy.append((-9.81-((self.vy[-1]+0.5*k_vy[-1])/abs(self.vy[-1]+0.5*k_vy[-1]))*(self.p*self.Cd*self.A/(2*self.mass))*(self.vy[-1]+0.5*k_vy[-1])**2)*self.dt)
            k_vx.append((-1*np.sign(self.vx[-1]+0.5*k_vx[-1])*(self.ro*self.Cd*self.A/(2*self.mass))*(self.vx[-1]+0.5*k_vx[-1])**2)*self.dt)
            k_vy.append((-9.81-np.sign(self.vy[-1]+0.5*k_vy[-1])*(self.p*self.Cd*self.A/(2*self.mass))*(self.vy[-1]+0.5*k_vy[-1])**2)*self.dt)
            k_x.append((self.vx[-1]+0.5*k_vx[-1])*self.dt)
            k_y.append((self.vy[-1]+0.5*k_vy[-1])*self.dt)
            self.vx.append(self.lista_vx[-1]+(k_vx[0]+2*k_vx[1]+2*k_vx[2]+k_vx[3])/6)
    
    


    def plot_trajectory(self):
        pozicije = np.array(self.pozicije)
        plt.plot(pozicije[:,0],pozicije[:,1])
        plt.xlabel('x pozicija')
        plt.ylabel('y pozicija')
        plt.title('projektil')
        plt.show()


projektil= particle(10,100,10,45)
projektil= plot_trajectory()











