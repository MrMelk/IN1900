import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4
from SIRD import Region, ProblemSIRD, SolverSIRD
from SIRD_interaction import RegionInteraction, ProblemInteraction

alpha = 7.5e-6
beta = 0.1/4
gamma = 0.9/4


def plague_Norway(alpha, beta, gamma, num_weeks, dt):
    Vestlandet = RegionInteraction(60, 5.3, "Vestlandet", 90000, 30, 0, 0)
    Sorlandet = RegionInteraction(58, 7.6, "SØrlandet", 65000, 0, 0, 0)
    Ostlandet = RegionInteraction(60, 11, "Østlandet", 80000, 0, 0, 0)
    Tronderlag = RegionInteraction(64, 11, "TrØnderlag", 70000, 0, 0, 0)
    Nord_Norge = RegionInteraction(69, 19, "Nord_Norge", 65000, 0, 0, 0)
    
    RegionList = [Vestlandet, Sorlandet, Ostlandet, Tronderlag, Nord_Norge]

    problem = ProblemInteraction(RegionList, alpha, beta, gamma)#hvorfor har jeg region igjen

    solver = SolverSIRD(problem, num_weeks, dt)
    #timepoints = np.linspace()
    solver.solve()
    plt.figure(figsize = (10, 10))
    index = 1
    for region in problem.region_name:
        plt.subplot(2,3,index)
        region.plot("time?")
        index += 1
    plt.subplot(2,3,index)
    problem.plot("time?")
    plt.legend()
    plt.show()

plague_Norway(alpha, beta, gamma, 104, 1/7)


