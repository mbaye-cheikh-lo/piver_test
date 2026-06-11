import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="piver_db",
        user="postgres",
        password="Bilidio18@"
    )