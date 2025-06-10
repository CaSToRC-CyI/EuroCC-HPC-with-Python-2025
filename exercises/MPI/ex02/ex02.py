import numpy as np
from mpi4py import MPI

rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

array = None
ntot = np.empty([], dtype=int)
sum_loc = np.empty([])
sum_tot = np.empty([])

if rank == 0:
    array = np.loadtxt("array.txt")
    ntot[()] = array.shape[0]

#
# TODO: Broadcast `ntot' to all processes
#

nloc = ntot // size
sub = np.empty(shape=nloc)

#
# TODO: Scatter `array[]' to all processes
#

sum_loc = np.sum(sub)

#
# TODO: Sum `sum_loc' over all ranks using a reduction operation
# 

if rank == 0:
    print(f" Sum: {sum_tot}")

