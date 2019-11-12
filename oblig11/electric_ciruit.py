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

def RS(L, R, I, Q, C, t):
    didt = (E(t) - R*I - Q/C)/L
    return didt
"""
def dqdt(I, t):
    return I
"""
class Electric:
    def __init__(self, L, R, I0, Q0, C, t):
        self.Q = Q0
        self.I = I0
        self.L = L
        self.R = R
        self.C = C
        self.t = t
    
    def __call__(self, u, t):#takes in a touple of Q and I values and returns it
       u_q = u[0]
       u_i = u[1]

       du_q = 1
       du_i = RS(self.L, self.R, u_i, u_q, self.C, self.t)
       return du_q, du_i

tp = np.linspace(0, 2*np.pi/(60*omega), n)

problem = Electric(L, R, I0, Q0, C, 0)
solver = RungeKutta4(problem)
u0 = (Q0, I0)
solver.set_initial_condition(u0)
u ,t = solver.solve(tp)

print(u)
plt.plot(t,u)
plt.show()

"""
class Electric:
    def __init__(self, L, R, I0, Q0, C, t):
        self.Q = Q0
        self.I = I0
        self.L = L
        self.R = R
        self.C = C
        self.t = t
    
    def __call__(self, u, t):#takes in a touple of Q and I values and returns it
        return dqdt(u, self.t), RS(self.L, self.R, u[1], u[0], self.C, self.t)


tp = np.linspace(0, 2*np.pi/(60*omega), n)

Electric_instance = Electric(L, R, I0, Q0, C, tp)
swag = RungeKutta4(Electric_instance)
swag.set_initial_condition((Q0,I0))

u, t = swag.solve(tp)
"""