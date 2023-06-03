import mysql.connector
import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv
import os

load_dotenv()
timezone = ZoneInfo("America/Sao_Paulo")

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
database = os.getenv("DB_DATABASE")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")

db_config = {
    'host': host,
    'user': user,
    'database': database,
    'password': password,
    'port': port
}

def get_connection():
    config = db_config
    cnx = mysql.connector.connect(**config)
    return cnx

def create_user(values):
    global timezone
    cnx = get_connection()
    cursor = cnx.cursor()
    
    data = datetime.datetime.now(timezone)
    print(f'Valores: {values}')
    values = list(values)
    
    if len(values) >= 4:  # Verificando se values tem pelo menos 4 elementos
        query = "INSERT INTO usuarios (nome, email, idade, salario, data_criacao) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (*values, data,))
    else:
        query = "INSERT INTO usuarios (nome, email, idade, data_criacao) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (*values, data,))
    
    print(f'Inserindo dados {values}')
    
    cnx.commit()
    cursor.close()
    cnx.close()
    
def get_user(email):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    
    query = "SELECT * FROM usuarios WHERE email = %s"
    cursor.execute(query, (email,))
    
    result = cursor.fetchone()
    
    cursor.close()
    cnx.close()
    
    return result
