from scipy import integrate
def func(x):
    return 3*x**2 + 5

result, err = integrate.quad(func, 0, 5)
print('result:{}, error:{}'.format(result, err))
