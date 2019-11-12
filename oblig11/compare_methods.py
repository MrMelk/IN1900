import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ODESolver
from ODESolver import RungeKutta4


class RungeKutta2(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        k1 = f(t[k - 1], u[k - 1])
        k2 = f(t[k-1] + 2/3*dt, u[k -1] + 2/3 * dt * k1)
        u_new = u[k - 1] + dt * (1/4*k1 + 3/4*k2)
        return u_new

class Heun(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        ustar = u[k-1] + dt * f(u[k], t[k-1])
        u_new = u[k-1] +1/2 * dt * f(u[k-1],t[k-1]) + 1/2 * dt * f(ustar, t[k])
        return u_new

def f(x, t):
    return x*np.cos(x) - np.sin(x)


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
From th eplots I get it seems they are ok ish approximations, however some of them get wayyy high with n = 20.
so it was hard to see how they matched up with higher steps. Removed some to see before i added them back
and if we remove some of the fewer steps they all look "decent". With the exception of RK4
that just goes up and stays in a line. RK2 looks definatly the best tho, even though it goes up and
down like crazy it moves in a wavey motion like it's supposed to
"""

