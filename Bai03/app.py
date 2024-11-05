from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import webbrowser
import threading
import time
import subprocess

app = Flask(__name__)
app.secret_key = '1234'

# Database configuration
DATABASE = {
    'dbname': 'test',
    'user': 'postgres',
    'password': 'Do12345678910..',
    'host': 'localhost',
    'port': '5555'
}

# Kết nối đến cơ sở dữ liệu
def get_db_connection():
    try:
        conn = psycopg2.connect(**DATABASE)
        return conn
    except psycopg2.DatabaseError as e:
        print(f"Database connection error: {e}")
        return None

@app.route('/')
def index():
    conn = get_db_connection()
    if conn is None:
        flash('Could not connect to the database.')
        return render_template('index.html', rows=[])

    with conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM danhsach')
            rows = cur.fetchall()
    
    return render_template('index.html', rows=rows)

@app.route('/insert', methods=['POST'])
def insert():
    hoten = request.form.get('hoten')
    diachi = request.form.get('diachi')

    if not hoten or not diachi:
        flash('Họ tên và địa chỉ không được để trống!')
        return redirect(url_for('index'))

    conn = get_db_connection()
    if conn is None:
        flash('Could not connect to the database.')
        return redirect(url_for('index'))

    with conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO danhsach (hoten, diachi) VALUES (%s, %s)', (hoten, diachi))
    
    flash('Dữ liệu đã được chèn thành công!')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    if conn is None:
        flash('Could not connect to the database.')
        return redirect(url_for('index'))

    with conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM danhsach WHERE id = %s', (id,))
    
    flash('Dữ liệu đã được xóa thành công!')
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset_database():
    conn = get_db_connection()
    if conn is None:
        flash('Could not connect to the database.')
        return redirect(url_for('index'))

    with conn:
        with conn.cursor() as cur:
            cur.execute('DROP TABLE IF EXISTS danhsach;')
            cur.execute('CREATE TABLE danhsach (id SERIAL PRIMARY KEY, hoten VARCHAR(100), diachi VARCHAR(255));')
    
    flash('Cơ sở dữ liệu đã được reset thành công!')
    return redirect(url_for('index'))

def run_app():
    app.run(debug=True, use_reloader=False)  # Disable reloader to avoid issues

if __name__ == '__main__':
    # Start the Flask app in a separate thread
    threading.Thread(target=run_app).start()
    
    # Open the browser
    webbrowser.open_new('http://127.0.0.1:5000/')

    # Wait for the user to close the browser window
    while True:
        time.sleep(1)  # Keep the main thread alive