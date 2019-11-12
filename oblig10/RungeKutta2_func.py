import numpy as np
import matplotlib.pyplot as plt

"""
Use the equaton from simple_ODE_func.py
du/dt = u/10

"""


n = 90



def f(t, u):
    dudt = u/10
    return dudt

#initial conditions
u0 = 0.2

x0 = 1

T = 20

def runge_kutta(f, u0, T, n):
    U = np.zeros(n+1)
    t = np.zeros(n+1)
    U[0] = u0
    t[0] = 0
    #t = np.linspace(0, T, n)
    #h = t[1] - t[0]
    dt = T/float(n)
    for i in range(1,n+1):
        t[i] = t[i-1] + dt
        k1 = f(t[i - 1], U[i - 1])
        k2 = f(t[i-1] + 2/3*dt, U[i -1] + 2/3 * dt * k1)
        U[i] = U[i - 1] + dt * (1/4*k1 + 3/4*k2)
    return U, t


RK = runge_kutta(f, u0, T, n)


def analytic(t):
    anal = np.zeros(len(t))
    for i in range(len(t)):
        anal[i] = 0.2 * np.exp(0.1*t[i])
    return anal

a = analytic(RK[1])

RK2 = runge_kutta(f, u0, T, 5)

plt.plot(RK[1], a, label = "anal")
plt.plot(RK[1], RK[0], label = f"runge-kutta n = {n}", ls = "--")
plt.plot(RK2[1], RK2[0], "r--", label = f"runge-kutta n = {6}")
plt.legend()
plt.xlabel("Timesteps")
plt.ylabel("Solution per timestep")
plt.show()

"""
run example:

It has been run and I got a kick ass plot yet again.

Tested with few timesteps, n = 6, and small, n = 90. when n = 90 the graphs looked identical
"""

