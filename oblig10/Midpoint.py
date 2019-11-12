import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ODESolver
from ODESolver import ForwardEuler


"""
y' = f(y, x) = cos(x) - xsin(x)
"""


class midpoint_euler(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self. f, self.k, self.t
        dt = t[k+1] - t[k]
        u_halv = u[k] + dt * f(u[k],t[k]) / 2
        u_new = u[k] + dt * f(u_halv, t[k] + dt/2)
        return u_new



def f(y, x):
    return np.cos(x) - x * np.sin(x)


def analytic(t):
    anal = np.zeros(len(t))
    for i in range(len(t)):
        anal[i] = t[i] * np.cos(t[i])
    return anal


if __name__ == "__main__":
    y0 = -5 * np.cos(-5)

    tp = np.linspace(-5,5,20)


    FE = ForwardEuler(f)
    FE.set_initial_condition(y0)
    yFE, tFE = FE.solve(tp)

    ME = midpoint_euler(f)
    ME.set_initial_condition(y0)
    y, t = ME.solve(tp)

    a = analytic(tp)

    plt.plot(t, a, label = "analytic")
    plt.plot(t, y, label = "Euler midpoint", ls = "--")
    plt.plot(tFE, yFE, label = "Forward Euler", ls = "-.")
    plt.xlabel("time")
    plt.ylabel("Euler Midpoint Method")
    plt.legend()
    plt.show()



"""
Run example:
Looks like the method is implemented well and that euler midpoint is way better than forward euler
"""