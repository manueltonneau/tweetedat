#!/bin/bash

#SBATCH --job-name=exploitation
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=500GB
#SBATCH --time=24:00:00
#SBATCH --gres=gpu:0
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-user=mt4493@nyu.edu
#SBATCH --output=slurm_get_timestamp-%j.out

RANDOM_SAMPLE_PATH=$1
OUTPUT_FILENAME=$2

module purge
#module load anaconda3/2020.02

#source /scratch/mt4493/twitter_labor/code/envs/inference_env/bin/activate
singularity exec --overlay /scratch/mt4493/twitter_labor/code/envs/singularity/inference/env.ext3:ro \
	    /scratch/work/public/singularity/cuda11.1-cudnn8-devel-ubuntu18.04.sif \
	    /bin/bash -c "source /ext3/env.sh; python3 /scratch/mt4493/twitter_labor/code/tweetedat/script/estimate_timestamps.py \
--random_sample_path ${RANDOM_SAMPLE_PATH} \
--output_filename ${OUTPUT_FILENAME}