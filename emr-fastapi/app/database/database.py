import mysql.connector
from mysql.connector import Error


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost", user="root", password="aio2025", database="erm_system"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def execute_query(query, params=None):
    connection = get_db_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if query.strip().upper().startswith("SELECT"):
            result = cursor.fetchall()
        else:
            connection.commit()
            result = cursor.rowcount
        return result
    except Error as e:
        print(f"Error execute query: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
