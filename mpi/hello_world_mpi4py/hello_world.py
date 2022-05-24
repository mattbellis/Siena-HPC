#hello.py
from mpi4py import MPI
comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

print(f"hello world from process {rank} of size {size}")
