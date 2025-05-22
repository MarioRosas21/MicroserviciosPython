import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del .env

def get_connection():
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")

    print(f"DEBUG: host={host}, port={port}, user={os.getenv('DB_USER')}, db={os.getenv('DB_NAME')}")

    return mysql.connector.connect(
        host=host,
        port=int(port),  # Esta línea lanza el error si port == None
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

