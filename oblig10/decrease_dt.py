import numpy as np
import matplotlib.pyplot as plt


def f(x, t):
    swag = np.cos(6*t)/(1 + t + x)
    return swag

T = 10
U0 = 0
n = [20, 30, 35, 40, 50, 100, 1000, 10000]

def ForwardEuler(f, U0, T, n):
    """Solve u’=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1) # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t

for i in n:
    FE = ForwardEuler(f, U0, T, i)
    plt.plot(FE[1], FE[0], label = f"Forward Euler of n = {i}")

plt.legend()
plt.xlabel("Timesteps")
plt.ylabel("Forward Euler")
plt.show()


"""
run example
I get a plot with a lot of lines that move in a wave motion. it becomes smoother and smoother 
the higher n goes
"""