import numpy as np

a = np.zeros((2,3))
b = a.reshape((1,3,2,1))

c = np.zeros((20,20))
d = c.reshape((1,20,20,1))
print(d)