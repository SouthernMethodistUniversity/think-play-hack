#!/bin/bash
#SBATCH -J usenet
#SBATCH -o usenet_data/pickle_to_csv_%a.out
#SBATCH -p htc
#SBATCH --array=0-7
#SBATCH -c 1
#SBATCH --mem=7G

module purge
module load python

categories=(alt sci soc misc talk comp rec news)

cd usenet_data
python3 ../usenet_pickle_to_csv.py ${categories[${SLURM_ARRAY_TASK_ID}]}

