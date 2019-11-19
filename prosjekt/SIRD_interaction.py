import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4
from SIRD import ProblemSIRD
from SIRD import Region
from SIRD import SolverSIRD

R_earth = 64e4#63710  #km more correct than 64 * 10^4


class RegionInteraction(Region):
    def __init__(self, latitude, longitude):
        self.latitude = latitude * np.pi/180
        self.longitude = longitude * np.pi/180
        super()
    
    def distance(self, other):  #Other must be touple of (latitude, longitude) in degrees
        long_i = self.longitude
        lat_i = self.latitude
        long_j = other[1] * np.pi/180              #other.longitude
        lat_j = other[0] * np.pi/180               #other.longitude #other vil jo ikke ha longitude eller latitude dafuq?
        dist = R_earth * np.arccos(np.sin(lat_i) * np.sin(lat_j) + np.cos(lat_i) * np.cos(lat_j) * np.cos(np.abs(long_i - long_j)))
        return dist
    
    