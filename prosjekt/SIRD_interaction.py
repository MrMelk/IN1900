import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4
from SIRD import ProblemSIRD
from SIRD import Region
from SIRD import SolverSIRD

R_earth = 64e4#63710  #km more correct than 64 * 10^4


class RegionInteraction(Region):
    def __init__(self, latitude, longitude, name, S0, I0, R0, D0):
        self.latitude = latitude * np.pi/180
        self.longitude = longitude * np.pi/180
        super().__init__(name, S0, I0, R0, D0)
    
    def distance(self, other):  #Other must be touple of (latitude, longitude) in degrees
        long_i = self.longitude
        lat_i = self.latitude
        long_j = other[1] * np.pi/180              #other.longitude
        lat_j = other[0] * np.pi/180               #other.longitude #other vil jo ikke ha longitude eller latitude dafuq?
        dsigma = np.arccos(np.sin(lat_i) * np.sin(lat_j) + np.cos(lat_i) * np.cos(lat_j) * np.cos(np.abs(long_i - long_j)))
        if long_i == long_j and lat_i == lat_j:
            dist = 0
        else:
            dist = R_earth * dsigma
        return dist
    
class ProblemInteraction(ProblemSIRD):
    def __init__(self, regionInstances, region, alpha, beta, gamma):
        self.region_name = regionInstances
        #print(self.region_name[0].name)
        #names = [region.name for region in self.region_name]   #for å lage liste av navn
        super().__init__(region, alpha, beta, gamma)
    
    def get_population(self):
        self.total_population = [region.population for region in self.region_name]
    
    def set_initial_condition(self):
        self.first_list = [self.region.S0, self.region.I0, self.region.R0, self.region.D0 for region in self.region_name]
        #eller
        """
        first_list = []
        for i in range(len(self.region_name)):
            first_list.append(self.region_name[i].S0)
            first_list.append(self.region_name[i].I0)
            first_list.append(self.region_name[i].R0)
            first_list.append(self.region_name[i].D0)
        """

    def __call__(self, u, t):
        n = len(self.region_name)

        SIRD_list = [u[i:i+4] for i in range(0, len(u), 4)]
        
        """
        S_list = SIRD_list[t][0]
        I_list = SIRD_list[t][1]
        R_list = SIRD_list[t][2]
        D_list = SIRD_list[t][3]
        """

        derivative = []
        for i in range(n):
            S, I, R, D = SIRD_list[i]
            dS = 0
            dI = 0
            dR = 0
            dD = 0
            for j in range(n):
                I_other = I_list


