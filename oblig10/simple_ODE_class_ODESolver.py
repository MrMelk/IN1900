import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ForwardEuler

def f(u, t):
    dudt = u/10
    return dudt

#initial condistions
u0 = 0.2

def analytic(t):
    anal = np.zeros(len(t))
    for i in range(len(t)):
        anal[i] = 0.2 * np.exp(0.1*t[i])
    return anal


#time
time = np.linspace(0, 20, 200)
time2 = np.linspace(0,20, 8)


n = 200

OwO = ForwardEuler(f)
OwO.set_initial_condition(u0)   #OwO ideen skammlost stjaalet av min venn Morten Berg
u, t = OwO.solve(time)
u2, t2 = OwO.solve(time2)

a = analytic(t)

plt.plot(t, a, label = "analytic")
plt.plot(t,u, label = f"n = {200}", ls = "--")
plt.plot(t2, u2, label = f"n = {8}")
plt.ylabel("u")
plt.xlabel("time")
plt.legend()
plt.show()


f = open("ForwardEulerODE_Class_Solver.txt","w+")
f.write("U(t) t\n")
for i in range(len(u)):
    f.write(f"{u[i]:.3f} {t[i]:.3f}\n")

"""
Run example:
I get that swagg ass plot BOI Damn that curve is fine.
Same as the 2 others, get cleaner with more intervals of time, reducing the error and such

"""