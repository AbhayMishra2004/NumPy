import  numpy as np

# ARRAY OF ZEROES
ar_zero = np.zeros(4)
print(ar_zero)

# 2D ARRAY OF ZEROES
# 3 ROW AND 4 COLOUMN
ar_zero2 = np.zeros((3,4))
print(ar_zero2)

# ARRAT OF ONES
ar_one = np.ones(4)
print(ar_one)

# CREATE AN EMPTY ARRAY
# BUT ISME PREVIOS MEMORY KA DATA AA JATA HAI BY DEFAULT
ar_empty = np.empty(4)
print(ar_empty)

# ARRAY FILLED WITH RANGE
ar_range = np.arange(4)
print(ar_range)

# DIAGONAL ARRAY FILEED WITH ONE
ar_digonal = np.eye(3)
print(ar_digonal)

# ARRAY OF LINE SPACE
# START , STOP , AND NUMBER OF ELEMENT IN ARRAY
ar_lin = np.linspace(0 , 20 , num=10)
print(ar_lin)