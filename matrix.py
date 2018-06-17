import numpy as np
a = np.arange(15).reshape(3,5)
print(a)
print(a.shape)
b = np.arange(5).reshape(5)
print(b)
print(np.arange(10, 30, 5).reshape(1,4))
from numpy import pi
print(np.linspace(0,2,9))
print(np.linspace(0,2*pi, 18))
c = np.arange(24).reshape(2,3,4)

print( np.arange(5).reshape(1,5))
print('{},{}'.format(a,b))
print(c, end='\n\n')
print(a*b,end='\n\n')
print(a.dot(b),end='\n\n')
print(b.reshape(5,))

print(np.eye(3))
