import matplotlib.pyplot as plt
import numpy as np

class KosiHitac:
    def __init__(self):
        self.g = -9.81
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []

    def set_initial_conditions(self, v0, theta, x0, y0, dt):
        self.vx += [v0*np.cos(np.radians(theta))]
        self.vy += [v0*np.sin(np.radians(theta))]
        self.theta = theta
        self.x +=[x0]
        self.y += [y0]
        self.v0=v0
        self.dt=dt

    def __move(self):
        self.vx += [self.vx[len(self.vx)-1]]
        self.vy += [self.vy[len(self.vy)-1]+self.g*self.dt]
       
        self.x += [self.x[len(self.x)-1]+self.vx[len(self.vx)-1]*self.dt]
        self.y += [self.y[len(self.y)-1]+self.vy[len(self.vy)-1]*self.dt]

    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.title('Putanja gibanja')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

    def calculate_max_height(self):
        while self.y[-1] >= 0:
            self.__move()
        return max(self.y)

    def calculate_range(self):
        while self.y[-1] >= 0:
            self.__move()
        return self.x[-1]

    def calculate_max_speed(self):
        while self.y[-1] >= 0:
            self.__move()
        return max(self.vy)

    def hit_target(self, target_x, target_y, target_radius):
        target_hit = False
        min_distance = float('inf')

        while self.y[-1] >= 0:
            self.__move()

            distance = np.sqrt((self.x[-1] - target_x) ** 2 + (self.y[-1] - target_y) ** 2)
            if distance <= target_radius:
                target_hit = True
                break

            if distance < min_distance:
                min_distance = distance


        velicina=np.linspace(0,2*np.pi,1000)
        velicina_x= target_x + target_radius*np.cos(velicina)
        velicina_y=target_y + np.sin(velicina)

         
        plt.plot(self.x, self.y)
        plt.plot(velicina_x,velicina_y)
        plt.title('Putanja gibanja s metom')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

        if target_hit:
            print('Meta je pogođena!')
        else:
            print('Meta nije pogođena. Najbliža udaljenost od mete: {:.2f}'.format(min_distance))
