import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4


"""
u' = -au
"""
#a
u0 = 1
a = np.log(2)/5600
class Decay:
    def __init__(self, a):
        self.a = a
    
    def __call__(self, u, t):
        return -self.a * u

#b
decay_inst = Decay(a)

#c
T = 20000
tp = np.linspace(1, T, T/500)
RK = RungeKutta4(decay_inst)
RK.set_initial_condition(u0)

u, t = RK.solve(tp)

def exact(t):
    return np.exp(-a * t)

print(f"Difference between exact, {exact(T):.5f}, and approxiamate {u[len(u)-1]:.5f}, is {np.abs(exact(T) - u[len(u)-1]):.5f} after {T} years. limited to  decimals")


plt.plot(t, u, label = "approximate fraction of particals that remain")
plt.plot(t, exact(t), label= "Exact fraction of particals that remain", ls = "--"   )
plt.legend()
plt.xlabel("t[y]")
plt.ylabel("u(t)")
plt.show()


"""
Get a swag ass plot and can see that it fitsa with the exact solution.
idk what more to write since this is the same as the past ones and not much more to comment

"""