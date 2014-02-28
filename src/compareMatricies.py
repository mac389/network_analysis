import numpy as np
import numpy.linalg as la

#Note that the two arrays must be the same size to
#allow the program to work properly.
matrix1 = np.eye(5)
matrix2 = np.eye(5)
matrix2[1][1] += 1

a, vectors1 = la.eig(matrix1)
a, vectors2 = la.eig(matrix2)

cosinesBetween = np.zeros(shape=(len(matrix1), len(matrix1)))

for i in range(0, len(vectors1)):
    print np.dot(vectors1[i],vectors2[i])/la.norm(vectors1[i])/la.norm(vectors2[i])
    #The above mess was taken from http://stackoverflow.com/a/2827466


#For some reason, the implementation of Python I'm using apparently considers the two
#matricies to be equal, even if I use the "==" operator builtin. No idea why.
#  (Note: Based on the output, I assume that "==" compares each element
#   element individually. Is this true?)
