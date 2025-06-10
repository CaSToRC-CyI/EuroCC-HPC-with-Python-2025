#!/bin/bash
#SBATCH --job-name=04
#SBATCH --nodes=2
#SBATCH --ntasks=8
#SBATCH --ntasks-per-node=4
#SBATCH --output=ex04-output.txt
#SBATCH --time=00:01:00
#SBATCH --reservation=edu27
#SBATCH -A edu27

module load SciPy-bundle/2024.05-gfbf-2024a mpi4py/4.0.1-gompi-2024a
mpirun python ex04.py
