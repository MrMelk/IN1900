from math import pi

q = 1.2 #density of air
V_soft = 30/3.6 #m/S
V_hard = 120/3.6    #m/S
m = 0.43    #kg
a = 11  #cm radius
A = pi*a**2 #Area
C_d = 0.4   #drag coefficient
g = 9.81    #gravity
Fg = m*g    #gravity force
Fd_soft = 1/2*C_d*q*A*V_soft**2
Fd_hard = 1/2*C_d*q*A*V_hard**2

print(f"{Fd_soft} is the drag force for a soft kick")
print(f"{Fd_hard} is the drag force for a hard kick")
print(f"{Fg} is the gravity force")