import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4
from SIRD import Region, ProblemSIRD, SolverSIRD
from SIRD_interaction import RegionInteraction, ProblemInteraction
from random import randint





alpha = 7e-6
beta = 0.1/4
gamma = 0.9/4


def plague_Norway(alpha, beta, gamma, num_weeks, dt):
    Vestlandet = RegionInteraction(60, 5.3, "Vestlandet", 90000, 30, 0, 0)
    Sorlandet = RegionInteraction(58, 7.6, "Sørlandet", 65000, 0, 0, 0)
    Ostlandet = RegionInteraction(60, 11, "Østlandet", 80000, 0, 0, 0)
    Tronderlag = RegionInteraction(64, 11, "TrØnderlag", 70000, 0, 0, 0)
    Nord_Norge = RegionInteraction(69, 19, "Nord_Norge", 65000, 0, 0, 0)
    
    RegionList = [Vestlandet, Sorlandet, Ostlandet, Tronderlag, Nord_Norge]

    problem = ProblemInteraction(RegionList, alpha, beta, gamma, "Noreg")

    solver = SolverSIRD(problem, num_weeks, dt)

    solver.solve()
    plt.figure(figsize = (10, 10))
    index = 1
    for region in problem.region:
        plt.subplot(2,3,index)
        region.plot("time?")
        index += 1
    plt.subplot(2,3,index)
    problem.plot("time?")
    plt.legend()
    plt.show()


plague_Norway(alpha, beta, gamma, 104, 1/7)

def alpha(t):   #defining a new alpha worksthough it may be suboptimal as an alpha variable has already been set, where the variable is a function. But hey if it works I guess
    if 0 <= t <= 2:
        return 3e-5
    elif 4 <= t <= 19:
        return 6e-6
    elif 24 <= t <= 41:
        return 6e-6
    elif 49 < t <= 75:
        return 7e-6
    else:
        return 1e-6

plague_Norway(alpha, beta, gamma, 104, 1/7)



def pesta(t):
    number = randint(0,20)
    if number == 13:
        return 10 * alpha(t)
    elif number == 4:
        return 5 * alpha(t)
    else:
        return 0.4 * alpha(t)
print("pesta")
plague_Norway(pesta, beta, gamma, 104, 1/7)

"""
Get plots for all the stuff. Pesta seems to be most present in Vestlandet and Østlandet, mostly Vestlandet. However she was present often in all.
Then again it's also random so who knows what it'll be next time
"""
