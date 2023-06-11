from kosi_hitac import KosiHitac

p = KosiHitac()

v0 = 10  
theta = 45  
x0 = 0  
y0 = 0  
dt = 0.01  

p.set_initial_conditions(v0, theta, x0, y0, dt)

# Izračunavanje i ispisivanje rezultata
print('Maksimalna visina:', p.calculate_max_height())
print('Domet:', p.calculate_range())
print('Maksimalna brzina:', p.calculate_max_speed())

# Testiranje funkcionalnosti hit_target()
target_x = 10
target_y = 5
target_radius = 1
p.hit_target(target_x, target_y, target_radius)


p.plot_trajectory()
