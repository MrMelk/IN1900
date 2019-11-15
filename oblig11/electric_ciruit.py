import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4

n = 10
L = 1   #H
omega = np.sqrt(3.5)    #s^(-2)
def E(t):
    return 2*np.sin(omega*t)

C = 0.25    #C
R = 0.2     #ohm
I0 = 1      #A
Q0 = 1    #C

#dt = 2*np.pi/(60*omega)



class Electric:
    def __init__(self, L, R, C, t):
        self.L = L
        self.R = R
        self.C = C
        self.t = t
    
    def __call__(self, u, t):#takes in a touple of Q and I values and returns it
        didt = (E(t) - self.R*u[1] - u[0]/self.C)/self.L

        
        dqdt = u[1]

        return dqdt, didt



dt =  2 * np.pi/(60 * omega)

T = 10 * (2 * np.pi/omega)
N = round(T / dt)
tp = np.linspace(0, T, N)

problem = Electric(L, R, C, 0)


solver = RungeKutta4(problem)

u0 = ([I0, Q0])
solver.set_initial_condition(u0)
u ,t = solver.solve(tp)

print(len(u))
print(len(t))

plt.plot(t, u)

plt.show()
"""
Get a swaggy plot that moves all wavy like inbetween each other

"""