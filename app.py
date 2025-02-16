from flask import Flask, request, jsonify
import psycopg2
import os
import logging

app = Flask(__name__)

# Configuring logging
logging.basicConfig(level=logging.DEBUG)

# Database connection
import time

def get_db_connection():
    retries = 5
    for i in range(retries):
        try:
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD')
            )
            return conn
        except Exception as e:
            logging.error(f"Database connection failed (attempt {i + 1}/{retries}): {e}")
            time.sleep(2)  # Wait for 2 seconds before retrying
    return None

@app.route('/')
def home():
    return "Welcome to the Staff API!"

@app.route('/staff', methods=['POST'])
def create_staff():
    data = request.get_json()
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Internal Server Error'}), 500
    try:
        cur = conn.cursor()
        cur.execute('INSERT INTO staff (first_name, last_name) VALUES (%s, %s) RETURNING id;',
                    (data['first_name'], data['last_name']))
        staff_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'id': staff_id}), 201
    except Exception as e:
        logging.error(f"Error creating staff: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/staff/<int:staff_id>', methods=['GET'])
def get_staff(staff_id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Internal Server Error'}), 500
    try:
        cur = conn.cursor()
        cur.execute('SELECT id, first_name, last_name FROM staff WHERE id = %s;', (staff_id,))
        staff = cur.fetchone()
        cur.close()
        conn.close()
        if staff is None:
            return jsonify({'error': 'Staff not found'}), 404
        return jsonify({'id': staff[0], 'first_name': staff[1], 'last_name': staff[2]})
    except Exception as e:
        logging.error(f"Error retrieving staff: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
