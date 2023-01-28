


import numpy as np

y = np.array([-6.00000, -5.89483, -5.65014, -5.17788, -4.28172, -3.99583])

q = np.zeros((6, 6 - 1))

print("==================================")

print(q)

print("==================================")

print(y[:, None])

print("==================================")

AAA = np.concatenate((y[:, None], q), axis=1)
print(AAA)

w = np.array([7,7,7,7,7,7])

print (np.concatenate((w[:, None], AAA), axis=1))

