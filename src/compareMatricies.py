import numpy as np

#Note that the two arrays must be the same size to
#allow the program to work properly.
matrix1 = np.eye(5)
matrix2 = np.eye(5)

a, vectors1 = la.eig(matrix1)
a, vectors2 = la.eig(matrix2)

cosinesBetween = np.zeros(shape=(len(matrix1), len(matrix1)))

def magnitude(vector):
    sum = 0
    for dim in vector:
        sum += (dim**2)
    return sum ** (0.5)

for i in range(0, len(vectors1)):
    print np.dot(vectors1[i],vectors2[i])/(magnitude(vectors1[i])*la.norm(vectors2[i]))

#For some reason, the implementation of Python I'm using apparently considers the two
#matrices to be equal, even if I use the "==" operator builtin. No idea why.
#  (I had manually set the second array to be the identity matrix times 2)
#  (Note: Based on the output, I had assumed that "==" compares each element
#   element individually. Is this true?)
