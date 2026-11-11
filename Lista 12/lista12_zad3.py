import numpy as np

n = 5
ciąg = np.arange(1, n+1)

a = 1/ciąg
print(a)

b = 1/2**(ciąg)
print(b)

c = 1/ciąg * b
print(c)

d= np.cumsum(c)
print(d)