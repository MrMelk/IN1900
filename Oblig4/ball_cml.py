import sys as sys 

v0 = int(sys.argv[1])
g = 9.81
t = int(sys.argv[2])
y = v0*t - 0.5*g*t**2
print(y)