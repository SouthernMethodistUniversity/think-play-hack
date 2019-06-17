#!/bin/bash
#SBATCH -J usenet
#SBATCH -o usenet_data/usenet_%a.out
#SBATCH -p htc
#SBATCH --array=0-17064
#SBATCH -c 1
#SBATCH --mem=6G

n=$(echo "${SLURM_ARRAY_TASK_ID}+40000" | bc)
#n=${SLURM_ARRAY_TASK_ID}

module purge
module load python

python3 usenet_clean.py sub_newsgroups.txt ${SLURM_JOB_ID} ${n} "usenet_data/${n}.pickle"

