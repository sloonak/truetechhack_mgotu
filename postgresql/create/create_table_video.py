import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="video_analyze", user='postgres', password='mynewpassword', host='localhost', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Creating table as per requirement
sql ='''DROP TABLE IF EXISTS video;
CREATE TABLE video ( id SERIAL PRIMARY KEY, url VARCHAR(1024), status VARCHAR(255), data JSONB , datetime TIMESTAMP);
CREATE INDEX url ON video (url);'''

cursor.execute(sql)
print("Table created successfully........")
conn.commit()
#Closing the connection
conn.close()