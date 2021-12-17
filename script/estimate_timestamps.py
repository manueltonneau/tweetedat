from TimestampEstimator import find_tweet_timestamp
import logging
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def get_args_from_command_line():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--random_sample_path", type=str, help="Name of the folder where keys are stored")
    parser.add_argument("--output_filename", type=str)

    args = parser.parse_args()
    return args

def get_timestamp_from_tweet_id(tweet_id):
    tstamp = find_tweet_timestamp(tweet_id)
    utcdttime = datetime.utcfromtimestamp(tstamp / 1000)
    return pd.to_datetime(utcdttime)

def main():
    args = get_args_from_command_line()
    df = pd.concat([pd.read_parquet(path) for path in Path(args.random_sample_path).glob('*.parquet')])
    logger.info('Scores loaded')
    df['tweet_id'] = df['tweet_id'].astype(int)
    df['datetime'] = df['tweet_id'].apply(get_timestamp_from_tweet_id)
    df.to_parquet(f'/scratch/spf248/twitter/data/random_samples/random_samples_splitted/{args.output_filename}.parquet', index=False)

if __name__ == '__main__':
    main()
