import os
import mysql.connector
from dotenv import load_dotenv

def conn():
    load_dotenv()

    mydb = mysql.connector.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        database=os.getenv('database'),
        charset='utf8mb4'
    )
    return mydb
