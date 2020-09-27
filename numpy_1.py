import numpy as np
# Converting a list to np array
li = [[1,2,3],[4,5,6]]
print(np.array(li), end="\n \n")
#generating a range of values with the optional distance parameter
rnge = np.arange(1,28,3)
print(rnge, end="\n \n")

#zeroes
z = np.zeros(5)
print(z, end="\n \n")
# zeroes - multidimensional
zeros = np.zeros((4,5))
print(zeros, end="\n \n")
#ones
o = np.ones(5)
print(o, end="\n \n")
#Ones - multidimensional
ones = np.ones((3,3))
print(ones, end="\n \n")
#Identity Matrix
i = np.eye(6)
print(i, end="\n \n")