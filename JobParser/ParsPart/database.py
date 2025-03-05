import mysql.connector

DB_CONFIG = {
    "host": "mysql_parser",
    "user": "parser_user",
    "password": "password123",
    "database": "parser_db"
}

def get_db():
    return mysql.connector.connect(**DB_CONFIG)

def query_db(query, args=(), one=False):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute(query, args)
    result = cursor.fetchall()
    cursor.close()
    return (result[0] if result else None) if one else result

def insert_jobs(jobs):
    db = get_db()
    cursor = db.cursor()
    cursor.executemany("""
        INSERT INTO jobs (title, company, salary, experience, city) 
        VALUES (%s, %s, %s, %s, %s)
    """, jobs)
    db.commit()
    cursor.close()