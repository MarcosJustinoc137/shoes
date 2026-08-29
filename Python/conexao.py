import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def conectar():
    conn = psycopg2.connect(
        dbname="Projeto",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        port="5432"
    )

    return conn
