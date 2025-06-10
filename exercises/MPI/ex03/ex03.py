import numpy as np
from mpi4py import MPI

#
# Computes the Fletcher 32 checksum of a byte stream in `data' with
# `length' number of elements
#
def fletcher32(data, length):
    w_len = length
    c0 = 0
    c1 = 0
    x = 0

    while w_len >= 360:
        for i in range (360):
            c0 = c0 + ord(data[x])
            c1 = c1 + c0
            x = x + 1
        c0 = c0 % 65535
        c1 = c1 % 65535
        w_len = w_len - 360

    for i in range (w_len):
       c0 = c0 + ord(data[x])
       c1 = c1 + c0
       x = x + 1
    c0 = c0 % 65535
    c1 = c1 % 65535
    return (c1 << 16 | c0)

#
# Get rank and number of processes
#
rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()

#
# Root rank reads all filenames
#
fnames = None
if rank == 0:
    fnames = open("filenames.txt", "r").readlines()

#
# Root rank scatters filenames, 1 to each process
#
fname = MPI.COMM_WORLD.scatter(fnames)

#
# Strip any potential newline characters or trailing spaces
#
fname = fname.strip()

#
# Each process reads their file and computes the checksum in `f'
#
data = open(fname, "rb").read().decode()
n = len(data)
f = fletcher32(data, n)

#
# Turn `f' into an array so that we can send it
#
f = np.array([f])

#
# Root process should allocate enough space to gather checksums
#
checksums = None
if rank == 0:
    checksums = np.zeros([len(fnames)], dtype=f.dtype)

#
# TODO: Use an appropriate Gather operation to collect checksums in root process
#


if rank == 0:
    #
    # Loop over checksums, printing to screen
    #
    for fn,checksum in zip(fnames, checksums):
        print("{:>15} -> {:08X}".format(fn.strip(), checksum))

