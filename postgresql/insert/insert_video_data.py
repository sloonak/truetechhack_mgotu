import psycopg2
import json

from postgresql import get_connection 


def insert_video_data(url = '', status = 'FAILED', data = ''):

    if not data:
        return

    #Establishing the connection
    conn = get_connection.get_conn()

    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database.
    cursor.execute('''INSERT INTO video(url, status, data, datetime) VALUES (%s, %s, %s, NOW())''', (url, status, json.dumps(data)))

    # Commit your changes in the database
    conn.commit()
    print("Records inserted........")

    # Closing the connection
    conn.close()