import numpy as np
import matplotlib.pyplot as plt
import sys

args = sys.argv
r_size = int(args[1])
#a = np.arange(9).reshape(3,3)
a = np.random.randint(-9, 10, size=(r_size ,r_size))
#a = np.array([[2,1],[1,1]])
b = np.random.randint(-9, 10, size=(r_size, 1))
#b = np.array([[5],[1]])
#print(np.linalg.inv(a))
print(np.linalg.matrix_rank(a))
a_i = np.linalg.inv(a)
c = a_i.dot(b)
print('ans = {}'.format(c))
print('{}*x={}'.format(a,b))
