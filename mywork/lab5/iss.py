import requests
import logging
import mysql.connector
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

URL = "http://api.open-notify.org/iss-now.json"

HOST = "ds2002.cgls84scuy1e.us-east-1.rds.amazonaws.com"
USER = "ds2002"
PASSWORD = "Xf3$fa57CwD!"
DATABASE = "iss"

REPORTER_ID = "dad8hw"
REPORTER_NAME = "Ishneet Bhatia"


def connect_db():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )


def register_reporter():
    db = None
    cursor = None

    try:
        db = connect_db()
        cursor = db.cursor()

        check_query = "SELECT reporter_id FROM reporters WHERE reporter_id = %s"
        cursor.execute(check_query, (REPORTER_ID,))
        result = cursor.fetchone()

        if result is None:
            insert_query = """
            INSERT INTO reporters (reporter_id, reporter_name)
            VALUES (%s, %s)
            """
            cursor.execute(insert_query, (REPORTER_ID, REPORTER_NAME))
            db.commit()
        else:
            logger.info("Reporter already exists.")

    except mysql.connector.Error as err:
        logger.error(f"Database error: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if db is not None and db.is_connected():
            db.close()


def extract():
    logger.info("Getting data from ISS API")
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    return response.json()


def load_to_db(data):
    db = None
    cursor = None

    try:
        db = connect_db()
        cursor = db.cursor()

        message = data["message"]
        latitude = float(data["iss_position"]["latitude"])
        longitude = float(data["iss_position"]["longitude"])

        timestamp = datetime.utcfromtimestamp(
            data["timestamp"]
        ).strftime("%Y-%m-%d %H:%M:%S")

        insert_query = """
        INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id)
        VALUES (%s,%s,%s,%s,%s)
        """

        cursor.execute(
            insert_query,
            (message, latitude, longitude, timestamp, REPORTER_ID)
        )

        db.commit()

    except mysql.connector.Error as err:
        logger.error(f"Database error: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if db is not None and db.is_connected():
            db.close()


def main():
    register_reporter()
    data = extract()
    load_to_db(data)
    logger.info(f"Inserted ISS record: {data}")


if __name__ == "__main__":
    main()