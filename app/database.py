# This file: read the DATABASE_URL from .env file
#            create a connection to PostgreSQL
#            expose a function that returns that connection to whoever needs it

import os
from dotenv import load_dotenv
import psycopg2 

load_dotenv()

def get_connection():
    database_url = os.getenv("DATABASE_URL")
    connection = psycopg2.connect(database_url)
    return connection


