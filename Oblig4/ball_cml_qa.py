import sys as sys 
try:
    v0 = int(sys.argv[1])
except IndexError:
    v0 = int(input("give missing v0 value: "))
g = 9.81
try:
    t = int(sys.argv[2])
except IndexError:
    t = int(input("give missing t value : "))
y = v0*t - 0.5*g*t**2
print(y)