import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4

alpha = 6.5e-5
beta = 0.1/4
gamma = 0.9/4

dt = 1

t = np.linspace(0, 63, 63)


def solvelolve(u, t):
    S0 = u[0]
    I0 = u[1]
    R0 = u[2]
    D0 = u[3]
    ds = -alpha*S0*I0
    di = alpha*S0*I0 - beta*I0 - gamma*I0
    dr = beta*I0
    dd = gamma*I0
    return(ds, di, dr, dd)

def terminate(u, t, k):#k er tidsstek mah BOI/GRILL
    u_k = u[k, :]
    u_k_minus_1 = u[k-1, :]
    test = np.abs(np.sum(u_k_minus_1) - np.sum(u_k))
    tol = 1e-9

    msg = "They aint the same bro. THEY AINT THE SAME"
    if test < tol:
        return False
    else:
        print(msg)
        return True






U0 = (7000, 30, 0, 0)

swaggyboi = RungeKutta4(solvelolve)
swaggyboi.set_initial_condition(U0)

u, t = swaggyboi.solve(t, terminate = terminate)


def plottelott(u, t):
    S = []
    I = []
    R = []
    D = []
    for i in range(len(u)):
        S.append(u[i][0])
        I.append(u[i][1])
        R.append(u[i][2])
        D.append(u[i][3])

    plt.plot(t, S, label = "S, healthy but may get the illness")
    plt.plot(t, I, label = "I, infected")
    plt.plot(t, R, label = "R, recovered, immune")
    plt.plot(t, D, label = "D, they fucin dead bro")
    plt.legend()
    plt.xlabel("Time in days")
    plt.ylabel("Populations")
    plt.show()

def test_zero():
        for i in range(1, len(u)):
            start_values = float(u[0][0] + u[0][1] + u[0][2] + u[0][3])
            testing_values = float(u[i][0] + u[i][1] + u[i][2] + u[i][3])
            tol = 1e-6
            assert np.abs(start_values - testing_values) < tol


plottelott(u, t)
if __name__ =="__main__":
    test_zero()    



"""
def solving(u, t):
    S0 = u[0]
    I0 = u[1]
    R0 = u[2]
    D0 = u[3]
    S =  -alpha*S0*I0
    I = alpha*S0*I0 - beta*I0 - gamma*I0
    R = beta*I0
    D = gamma*I0
    return (S, I, R, D)
    


def plotting(u, t):
    for i in range(len(u)-1):
        plt.plot(t,u[i])
    
    plt.show()


U0 = (7000, 30, 0, 0)

swaggyboi = RungeKutta4(solving)
swaggyboi.set_initial_condition(U0)
u, t = swaggyboi.solve(t)
print(len(u))
print(len(t))

print(u)
#plotting(u, t)
"""


