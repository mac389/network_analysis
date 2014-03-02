import numpy as np
import matplotlib.pyplot as plt

from numpy import linalg as la
from pprint import pprint
from matplotlib import rcParams

rcParams['text.usetex'] = True
#Note that the two arrays must be the same size to
#allow the program to work properly.

format = lambda text: r'\Large \textbf{%s}'%text

ndims = 5
repeats = 2

weights = 0
vectors = 1

matrices = [np.eye(ndims)] * repeats


def similarity(matrices, visualize=False):
	#Assume input is a list of matrices
	eigendecomposition = map(la.eig,matrices)
	answer = np.zeros((ndims,ndims,len(eigendecomposition),len(eigendecomposition)))
	for i in xrange(len(eigendecomposition)):
		for j in xrange(i):

			one = eigendecomposition[i][vectors]
			two = eigendecomposition[j][vectors]
			
			answer[:,:,i,j] = one.dot(two) 

			if visualize:

				fig = plt.figure()
				ax = fig.add_subplot(111)

				cax = ax.imshow(answer[:,:,i,j],aspect='auto',interpolation='nearest')
				cbar = plt.colorbar(cax)

				ax.set_ylabel(r'\Large \textbf{Eigenvectors of matrix %d}'%i)
				ax.set_xlabel(r'\Large \textbf{Eigenvectors of matrix %d}'%j)
				cbar.set_label(r'\Large $\mathbf{\cos \; \theta}$', rotation='horizontal')

				plt.tight_layout()
				plt.savefig('comparison-%d-%d.png'%(i,j),dpi=200)
	return answer

def angle(one,two):
	return np.dot(one,two)/float(la.norm(one)*la.norm(two))


similarities = similarity(matrices, visualize=True)
