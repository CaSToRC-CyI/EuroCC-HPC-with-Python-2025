import numpy as np
from mpi4py import MPI

#
# Get rank and number of processes
#
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

#
# Initialize arrays and variables
#
array = None
ntot = np.empty([], dtype=int)
sum_loc = np.empty([])
sum_tot = np.empty([])

#
# Root rank reads entire array and number of elements in array `ntot'
#
if rank == 0:
    array = np.loadtxt("array.txt")
    ntot[()] = array.shape[0]

#
# TODO: Broadcast `ntot' to all processes
#


#
# Each rank computes local number of elements and allocates space for
# sub-array with nloc+2 elements
#
nloc = ntot // size
sub = np.empty(shape=(nloc+2))

#
# TODO: Scatter `array[]' to `sub[1:-1]' of each process
#


#
# Compute the ranks of the immediate neighbors, i.e. of the next and previous processes
#
rank_f = (rank+1)%size       # <-- rank in the forward direction
rank_b = (size+rank-1)%size  # <-- rank in the backward direction

#
# TODO: Use a Sendrecv to
#   - send the appropriate element of `sub[]' to the process in the backward direction
#   - receive the message from the rank in the forward direction and store it in `sub[-1]'
#

#
# TODO: Use a Sendrecv to
#   - send the appropriate element of `sub[]' to the process in the forward direction
#   - receive the message from the rank in the backward direction and store it in `sub[0]'
#


#
# Compute the second-derivative locally
#
deriv_loc = np.roll(sub, +1) + np.roll(sub, -1) - 2*sub


#
# Allocate space needed to gather global derivative at root
#
deriv = np.empty([ntot])

#
# TODO: Gather `deriv[]' into rank = 0. Need to omit sending the
#       edges, namely `deriv_loc[0]' and `deriv_loc[-1]'
#

if rank == 0:
    #
    # Root process writes global derivative to a text file
    #
    np.savetxt("deriv.txt", deriv, fmt="%+8.6f")
