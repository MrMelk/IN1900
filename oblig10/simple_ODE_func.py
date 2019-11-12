import numpy as np
import matplotlib.pyplot as plt

"""
want to solver u - 10*u' = 0. u(0) = 0.2
Blir u' = u/10
"""


def f(u, t):
    dudt = u/10
    return dudt

#initial condistions
u0 = 0.2

#steps
n = 200


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

def analytic(t):
    anal = np.zeros(len(t))
    for i in range(len(t)):
        anal[i] = 0.2 * np.exp(0.1*t[i])
    return anal


FE = ForwardEuler(f, u0, 20, n)
a = analytic(FE[1])
FE2 = ForwardEuler(f, u0, 20, 6)
plt.plot(FE[1], FE[0], label = f"n = {n}")
plt.plot(FE2[1], FE2[0], label = f"n = {6}", ls = "--")
plt.plot(FE[1], a, label = "analytic", ls ="-.")
plt.legend()
plt.xlabel("time [s]")
plt.ylabel("U[t]")
plt.show()

FEU = FE[0]
FET = FE[1]
f = open("ForwardEulerODE.txt","w+")
f.write("U(t) t\n")
for i in range(n+1):
    f.write(f"{FEU[i]:.3f} {FET[i]}\n")

"""

Run example:
Got a plot of the curved graph and results were written to my file. I chose a .txt file
because that felt normal for me to do and can easily be used to import it to a new program.

Can see the numerical solution comes closer to analytical the more steps we use

"""