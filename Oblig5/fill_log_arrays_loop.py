import numpy as np


X = np.linspace(1, 10, 101)
Y = np.zeros(len(X))
for i in range(len(X)):

    Y[i] = np.log(X[i])

print(X)
print(Y)
