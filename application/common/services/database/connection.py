import os
import psycopg2

connection = None


def get_db_connection():
    global connection
    if not connection:
        connection = psycopg2.connect(
            host="localhost",
            database=os.environ.get('POSTGRES_DB'),
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD']
        )
    return connection
