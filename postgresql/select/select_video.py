import psycopg2
import json

from postgresql import get_connection 


def select_video_by_url(url = ''):

    if not url:
        return

    #Establishing the connection
    conn = get_connection.get_conn()

    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    print(url)
    cursor.execute('''SELECT * FROM video WHERE url LIKE '/var/www/truetechhack/static/video/rik1080.mp4' ''')

    #Fetching 1st row from the table
    result = cursor.fetchone();

    #Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()

    return result