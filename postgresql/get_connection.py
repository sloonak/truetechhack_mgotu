import psycopg2

def get_conn():
   DATABASE_USER = 'postgres'
   DATABASE_PASSWORD = 'mynewpassword'
   DATABASE_HOST = 'localhost'
   DATABASE_PORT = '5432'
   DATABASE_NAME = 'video_analyze'

   #Establishing the connection
   conn = psycopg2.connect(
      database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASSWORD, host=DATABASE_HOST, port= DATABASE_PORT
   )

   return conn
