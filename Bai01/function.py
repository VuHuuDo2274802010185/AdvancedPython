import psycopg2
from tkinter import messagebox

# Hàm kết nối với cơ sở dữ liệu PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5555",
            database="postgres",
            user="postgres",
            password="Do12345678910.."
        )
        return conn
    except Exception as e:
        messagebox.showerror("Database Connection Error", str(e))
        return None

# Hàm thêm dữ liệu vào bảng
def add_data(name, age):
    conn = connect_db()
    if conn:
        with conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute("INSERT INTO person (name, age) VALUES (%s, %s)", (name, age))
                    return "Data inserted successfully"
                except Exception as e:
                    return f"Failed to insert data: {str(e)}"

# Hàm xóa dữ liệu theo ID
def delete_data(id_to_delete):
    conn = connect_db()
    if conn:
        with conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute("DELETE FROM person WHERE id = %s", (id_to_delete,))
                    if cursor.rowcount > 0:
                        return f"Record with ID {id_to_delete} deleted successfully"
                    else:
                        return f"No record found with ID {id_to_delete}"
                except Exception as e:
                    return f"Failed to delete data: {str(e)}"

# Hàm chỉnh sửa dữ liệu theo ID
def edit_data(id_to_edit, new_name, new_age):
    conn = connect_db()
    if conn:
        with conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute("UPDATE person SET name = %s, age = %s WHERE id = %s", 
                                   (new_name, new_age, id_to_edit))
                    if cursor.rowcount > 0:
                        return f"Record with ID {id_to_edit} updated successfully"
                    else:
                        return f"No record found with ID {id_to_edit}"
                except Exception as e:
                    return f"Failed to update data: {str(e)}"

# Hàm xóa tất cả dữ liệu trong bảng
def reset_database():
    conn = connect_db()
    if conn:
        with conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute("DELETE FROM person")  # Xóa tất cả dữ liệu trong bảng person
                    cursor.execute("ALTER SEQUENCE person_id_seq RESTART WITH 1")  # Reset ID sequence to 1
                    return "All records deleted successfully and ID reset."
                except Exception as e:
                    return f"Failed to reset database: {str(e)}"

# Hàm lấy dữ liệu từ bảng và hiển thị
def display_data():
    conn = connect_db()
    if conn:
        with conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute("SELECT * FROM person")
                    rows = cursor.fetchall()
                    return rows
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to retrieve data: {str(e)}")
