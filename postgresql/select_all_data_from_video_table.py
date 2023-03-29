import psycopg2
import get_connection

#establishing the connection
conn = get_connection.get_conn()

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
# cursor.execute('''select column_name, data_type, character_maximum_length
 # from INFORMATION_SCHEMA.COLUMNS where table_name ='video';''')

cursor.execute('''SELECT * FROM video''')

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()