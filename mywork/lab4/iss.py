#!/usr/bin/env python3

import sys
import requests
import pandas as pd
import logging
import os


# set up logging so we can see what the script is doing
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def extract():
    """
    This function gets the ISS data from the API.
    """

    logger.info("Getting data from the ISS API")

    url = "http://api.open-notify.org/iss-now.json"

    try:
        response = requests.get(url)
        data = response.json()
        return data

    except Exception as e:
        logger.error("Something went wrong while getting data")
        logger.error(e)
        return None


def transform(data):
    """
    This function takes the JSON data and turns it into a table.
    It also converts the timestamp into normal date and time.
    """

    logger.info("Converting data into table format")

    timestamp = data["timestamp"]
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]

    # convert the timestamp into readable format
    time = pd.to_datetime(timestamp, unit="s")

    # put everything into a dataframe
    df = pd.DataFrame({
        "time": [time],
        "latitude": [latitude],
        "longitude": [longitude]
    })

    return df


def load(df, filename):
    """
    This function saves the data into a CSV file.
    If the file already exists, it adds the new row.
    """

    logger.info("Saving data to CSV file")

    if os.path.exists(filename):

        old_df = pd.read_csv(filename)

        new_df = pd.concat([old_df, df])

        new_df.to_csv(filename, index=False)

    else:

        df.to_csv(filename, index=False)

    logger.info("Done saving")


def main():
    """
    This runs the whole ETL process.
    """

    filename = sys.argv[1]

    data = extract()

    if data is not None:

        df = transform(data)

        load(df, filename)


if __name__ == "__main__":
    main()