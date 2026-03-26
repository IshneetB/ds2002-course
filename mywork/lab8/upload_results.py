import os
import glob
import argparse
import logging
import boto3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder")
    parser.add_argument("destination")
    args = parser.parse_args()
    return args.input_folder, args.destination


def upload(input_folder, destination):
    try:
        bucket, prefix = destination.split("/", 1)
        prefix = prefix.rstrip("/")

        s3 = boto3.client("s3", region_name="us-east-1")
        file_list = glob.glob(input_folder + "/results-*.csv")

        if len(file_list) == 0:
            logger.info("No results files were found.")
            return False

        for file_path in file_list:
            file_name = os.path.basename(file_path)
            s3_key = prefix + "/" + file_name

            with open(file_path, "rb") as f:
                s3.put_object(Bucket=bucket, Key=s3_key, Body=f)

            logger.info("Uploaded " + file_name)

        return True

    except Exception as e:
        logger.error("Error: " + str(e))
        return False


def main():
    input_folder, destination = parse_args()
    success = upload(input_folder, destination)

    if success:
        logger.info("Finished successfully.")
    else:
        logger.info("Finished with errors.")


if __name__ == "__main__":
    main()
