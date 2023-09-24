import numpy as np

# CREATION OF ARRAY
a = np.array([1,2,3])

# CHECK DIMENSION OF ARRAY
print(a.ndim)

# MULTI DIMENSIONAL ARRAY
tenDArray = np.array([1,2,3,4],ndmin=10)
print(tenDArray.ndim)
