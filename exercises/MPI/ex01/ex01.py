import socket

from mpi4py import MPI

#
# TODO: call the appropriate MPI functions here 
#
rank =  # TODO
size =  # TODO

hostname = socket.gethostname()

print(f"This is rank = {rank} of nproc = {size} on node: {hostname}")
