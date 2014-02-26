import numpy as np
import numpy.linalg as linalg

#Ripped from http://stackoverflow.com/a/2891805/1863564:
import contextlib
import numpy.core.arrayprint as arrayprint

@contextlib.contextmanager
def printoptions(strip_zeros=True, **kwargs):
  origcall = arrayprint.FloatFormat.__call__
  def __call__(self, x, strip_zeros=strip_zeros):
    return origcall.__call__(self, x, strip_zeros)
  arrayprint.FloatFormat.__call__ = __call__
  original = np.get_printoptions()
  np.set_printoptions(**kwargs)
  yield
  np.set_printoptions(**original)
  arrayprint.FloatFormat.__call__ = origcall

#End blatant copying

#The laplacian matrix for the network.
network = np.eye(10)
#Old matrix: [[1,-1,0,0,0,0,0,0,0,0],[-1,6,-1,-1,-1,0,0,0,-1,-1],[0,-1,2,0,-1,0,0,0,0,0],[0,-1,0,2,0,0,-1,0,0,0],[0,-1,-1,0,4,0,0,0,-1,-1],[0,0,0,0,0,1,-1,0,0,0],[0,0,0,-1,0,-1,2,0,0,0],[0,0,0,0,0,0,0,1,-1,0],[0,-1,0,0,-1,0,0,-1,4,-1],[0,-1,0,0,-1,0,0,0,-1,3]]
v, w = linalg.eig(network)

with printoptions(strip_zeros=False, precision=2, suppress=True):
  print(network)
  print(v)
  print(w)
