import numpy as np
a = np.arange(5,81,9)
a = a.reshape(3,3)
print('Original array is:')
print(a)
print('\n')
print('Modified array is:')
for x in np.nditer(a):
   print(x)
