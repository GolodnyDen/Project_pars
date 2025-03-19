import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "parser_user",
    "password": "password123",
    "database": "parser_db"
}

def get_db():
    try:
        print("Connecting to database...")
        db = mysql.connector.connect(**DB_CONFIG)
        print("Connected successfully!")
        return db
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        raise

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