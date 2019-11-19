import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ODESolver
from ODESolver import RungeKutta4


class RungeKutta2(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        bruh = dt * f(u[k], t[k])
        bruh2 = dt * f(u[k] + 1/2*bruh, t[k] + 1/2 * dt)
        u_new = u[k] + bruh2
        return u_new

class Heun(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        ustar = u[k] + dt * f(u[k], t[k])
        u_new = u[k] +1/2 * dt * f(u[k],t[k]) + 1/2 * dt * f(ustar, t[k])
        return u_new

def f(u, t):
    return t*np.cos(t) - np.sin(t)


def exact(x):
    return x*np.sin(x) + 2*np.cos(x)

y0 = exact(-17)




n = [20, 25, 50, 150]

plt.subplot(4,1,1)
plt.title("RungeKutta2")
for i in n:
    t = np.linspace(-17, 17, i)
    RK2 = RungeKutta2(f)
    RK2.set_initial_condition(y0)
    u, t = RK2.solve(t)
    plt.plot(t, u, label = f"n = {i} steps")
plt.legend()


plt.subplot(4,1,2)
plt.title("RungeKutta4")
for i in n:
    t = np.linspace(-17, 17, i)
    RK4 = RungeKutta4(f)
    RK4.set_initial_condition(y0)
    u, t = RK4.solve(t)
    plt.plot(t, u, label = f"n = {i} steps")
plt.legend()


plt.subplot(4,1,3)
plt.title("Heun")
for i in n:
    t = np.linspace(-17, 17, i)
    H = Heun(f)
    H.set_initial_condition(y0)
    u, t = H.solve(t)
    plt.plot(t, u, label = f"n = {i} steps")
plt.legend()


plt.subplot(4,1,4)
plt.title("Exact")
for i in n:
    t = np.linspace(-17, 17, i)
    u = exact(t)
    plt.plot(t, u, label = f"n = {i} steps")

plt.legend()
plt.show()

"""
From the plots I can see that rungekuta two and rungekutta 4 give the best approximations.
"""

