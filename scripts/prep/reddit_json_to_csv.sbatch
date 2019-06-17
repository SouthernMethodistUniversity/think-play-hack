#!/bin/bash
#SBATCH -J reddit
#SBATCH -o reddit_10-2007_03-2015/to_tsv_%a.out
#SBATCH -p htc
#SBATCH --array=0-92
#SBATCH -c 1
#SBATCH --mem=42G

module purge
export MODULEPATH+=":/hpc/modules/tph"
module --ignore-cache load apps

cd reddit_10-2007_03-2015
json_file=$(head -${SLURM_ARRAY_TASK_ID} json_files.txt | tail -1)

python3 ../reddit_json_to_csv.py ${json_file}

