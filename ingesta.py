import pandas as pd
import pymysql
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# --- Datos de conexión a MySQL ---
host = os.getenv("MYSQL_HOST")
port = int(os.getenv("MYSQL_PORT"))
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DB")

# --- Datos para S3 ---
s3_bucket = os.getenv("S3_BUCKET")
s3_file_key = os.getenv("S3_KEY", "salida.csv")

# --- Conexión MySQL e ingesta ---
conn = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

query = "SELECT * FROM peliculas"
df = pd.read_sql(query, conn)
conn.close()

# --- Guardar como CSV ---
file_path = "/programas/ingesta/salida.csv"
df.to_csv(file_path, index=False)

# --- Subir a S3 ---
s3 = boto3.client("s3")
s3.upload_file(file_path, s3_bucket, s3_file_key)

print("✅ Ingesta completada: datos MySQL → CSV → S3")
