import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4
from SIRD import ProblemSIRD
from SIRD import Region
from SIRD import SolverSIRD




class RegionInteraction(Region):
    def __init__(self, latitude, longitude, name, S0, I0, R0, D0):
        self.lat = latitude * np.pi/180
        self.lon = longitude * np.pi/180
        super().__init__(name, S0, I0, R0, D0)
    
        """def distance(self, other):  #Other must be touple of (latitude, longitude) in degrees
        long_i = self.longitude
        lat_i = self.latitude
        long_j = other.longitude * np.pi/180              #other.longitude
        lat_j = other.latitude * np.pi/180               #other.latitude
        dsigma = np.arccos(np.sin(lat_i) * np.sin(lat_j) + np.cos(lat_i) * np.cos(lat_j) * np.cos(np.abs(long_i - long_j)))
        test = np.sin(lat_i) * np.sin(lat_j) + np.cos(lat_i) * np.cos(lat_j) * np.cos(np.abs(long_i - long_j))
        
        if test > 1:
            return 0
        else:

            dist = R_earth * dsigma
        if self == other:
            return 0
        print(dist)
        return dist"""
    
    def distance(self, other):
        R=64
        inarccos = np.sin(self.lat)*np.sin(other.lat) + np.cos(self.lat)*np.cos(other.lat)*\
            np.cos(abs(self.lon - other.lon))
        if inarccos > 1:
            dsigma = 0
        else:
            dsigma = np.arccos(inarccos)
        
        dist = R * dsigma
        return dist
    
class ProblemInteraction(ProblemSIRD):
    def __init__(self, region, alpha, beta, gamma):
        self.region_name = region
        #print(self.region_name[0].name)
        #names = [region.name for region in self.region_name]   #for å lage liste av navn
        super().__init__(region, alpha, beta, gamma)
    
    def get_population(self):
        self.total_population = [region.population for region in self.region_name]
        self.total_population = np.sum(self.total_population)
        return self.total_population
    
    def set_initial_condition(self):
        #self.first_list = [region.S0, region.I0, region.R0, region.D0 for region in self.region_name]
        #eller
        
        not_nested_list = []
        for i in range(len(self.region_name)):
            not_nested_list.append(self.region_name[i].S0)
            not_nested_list.append(self.region_name[i].I0)
            not_nested_list.append(self.region_name[i].R0)
            not_nested_list.append(self.region_name[i].D0)
        self.U0 = not_nested_list
        #print(self.U0)
        

    def __call__(self, u, t):
        n = len(self.region_name)
        I_list = [u[i] for i in range(1, len(u), 4)]
        SIRD_list = [u[i:i+4] for i in range(0, len(u), 4)]
        
        self.derivative = []
        for i in range(n):
            S, I, R, D = SIRD_list[i]
            dS = 0
            alpha = self.alpha(t)
            beta = self.beta(t)
            gamma = self.gamma(t)
            
            for j in range(n):

                I_other = I_list[j]
                distance = self.region_name[i].distance(self.region_name[j])
                #print(distance)
                dS +=  -alpha * S * I_other*np.exp(-distance)
            dR = beta * I
            dD = gamma * I
            dI = - beta * I - gamma * I
            dI += -dS
        
            self.derivative += [dS, dI, dR, dD]
        #print("derive",self.derivative)
        return self.derivative

    def solution(self, u, t):
        n = len(t)
        n_reg = len(self.region)
        self.t = t
        self.S = np.zeros(n)
        self.I = np.zeros(n)
        self.R = np.zeros(n)
        self.D = np.zeros(n)
        SIRD_list = [u[:, i:i+4] for i in range(0, n_reg*4, 4)]
        #print(SIRD_list)
        for part, SIRD in zip(self.region_name, SIRD_list):
            part.set_SIRD_values(SIRD, t)
            #print("part",part.S0)
            self.S += part.S0
            self.I += part.I0
            self.R += part.R0
            self.D += part.D0


    def plot(self, x_label):
        self.name = [region.name for region in self.region_name]#spør tobias om dette går greit
        plt.title(self.name)
        plt.plot(self.t, self.S, label = "Susceptible", color = "Blue")
        plt.plot(self.t, self.I, label = "Infected", color = "Green")
        plt.plot(self.t, self.R, label = "Immune", color = "Yellow")
        plt.plot(self.t, self.D, label = "Deceased", color = "Black")
        plt.xlabel(x_label)
        plt.ylabel("Population")



        
