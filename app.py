# dependencies: Flask, psycopg2
from flask import Flask
import psycopg2

app = Flask(__name__)

# Sample database credentials (use environment variables in production!)
DB_HOST = 'localhost'       # or 'db' if using Docker Compose
DB_PORT = 5432
DB_NAME = 'mydatabase'
DB_USER = 'myuser'
DB_PASSWORD = 'mypassword'

@app.route('/')
def hello_world():
    return 'Hello, World! This is the Flask app running in a Docker container. This is the second version Deji update!'

@app.route('/db-status')
def check_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        conn.close()
        return '✅ Successfully connected to the database!'
    except Exception as e:
        return f'❌ Failed to connect to the database: {e}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
