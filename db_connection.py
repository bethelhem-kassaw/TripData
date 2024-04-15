import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        print("Connection to MySQL DB successful")
        return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
    

db_connection = get_db_connection()
if db_connection:
    print("Successfully connected to the database.")
else:
    print("Failed to connect to the database.")