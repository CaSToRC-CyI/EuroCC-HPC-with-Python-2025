#!/bin/bash
#SBATCH -J fletcher32
#SBATCH -o f32.txt
#SBATCH -e f32.err
#SBATCH -p cpu
#SBATCH -A edu27
#SBATCH --reservation=edu27
#SBATCH -t 00:02:00
#SBATCH -n 1
#SBATCH -N 1
#SBATCH --ntasks-per-node=1

module load Python

date +"%T.%6N"
srun python fletcher32.py /nvme/scratch/edu27/Intro/data/03.txt
date +"%T.%6N"