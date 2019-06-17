#!/bin/bash
#SBATCH -J reddit_process
#SBATCH -p standard-mem-m
#SBATCH --mem=250G
#SBATCH --mail-user=acambre@smu.edu
#SBATCH --mail-type=ALL

# the above comments are actually meta-commands that slurm picks up

# this, obviously, purges all modules
module purge

# this appends TPH to the MODULEPATH, allowing more modules to be seen. Apparently the "apps" module loads the Singularity container.
export MODULEPATH+=":/hpc/modules/tph"
module --ignore-cache load apps

# While this has the same name as my shell script, it is in fact an application (?) that invokes a symlink in the container that points
# to the actual script.
reddit_process
