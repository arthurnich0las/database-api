import mysql.connector

db_config = {
    'host': '31.220.54.159',
    'user': 'acessodb',
    'password': '123456789',
    'port': '3306'
}

def get_connection(database):
    config = db_config
    config['database'] = database
    cnx = mysql.connector.connect(**config)
    return cnx

def get_user(database, email):
    cnx = get_connection(database)
    cursor = cnx.cursor(dictionary=True)
    
    query = "SELECT * FROM usuarios WHERE email = %s"
    cursor.execute(query, (email,))
    
    result = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    return result
