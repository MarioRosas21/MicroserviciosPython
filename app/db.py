import mysql.connector
import os

# Solo carga .env en desarrollo local
if os.getenv("RENDER") is None:
    from dotenv import load_dotenv
    load_dotenv()

def get_connection():
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")

    # Validación básica para evitar errores por variables faltantes
    if not all([host, port, user, password, database]):
        raise Exception("Faltan variables de entorno necesarias para la conexión a la base de datos.")

    print(f"DEBUG: host={host}, port={port}, user={user}, db={database}")

    return mysql.connector.connect(
        host=host,
        port=int(port),
        user=user,
        password=password,
        database=database
    )
