#!/bin/bash
#
# Set Job Name
#SBATCH -J job

# Set file to capture standard out and standard error and append the jobID (%j)
#SBATCH -o job.out.%j

#Set the total number of nodes 
#SBATCH -N 2

#Set the total number of cores, across all nodes, to use for the job
#SBATCH -n 24

#Set the time limit for the job - one hour is specified here
#SBATCH --time=0:60:00

export SLURM_EXPORT_ENV=ALL

# Move to the directory needed - defaults to the submission directory
cd $SLURM_SUBMIT_DIR

#Load any necessary environmental modules here
module load Python3
module load OHPC/openmpi-3.1.4

# perform calculation
bash run.sh hello_world.py
