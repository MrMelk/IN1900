from math import e

#Bruker algebra for å finne C.
#N(0) = B/(1+C)
#(1+c)*N(0) = B
#C*N(0) = B - N(0)
#C = (B - N(0))/N(0)
B = 50000
C = (B - 5000)/5000
k = 0.2 #h^-1

N_24 = B/(1+C*e**(-k*24))
print (N_24)