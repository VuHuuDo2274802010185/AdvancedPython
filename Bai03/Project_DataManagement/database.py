import psycopg2
from config import DATABASE

def get_db_connection():
    """Tạo kết nối đến cơ sở dữ liệu PostgreSQL."""
    try:
        connection = psycopg2.connect(**DATABASE)
        print("Database connection established.")
        return connection
    except psycopg2.OperationalError as e:
        print(f"Operational error: {e}")
        return None
    except psycopg2.DatabaseError as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def close_db_connection(connection):
    """Đóng kết nối đến cơ sở dữ liệu."""
    if connection:
        connection.close()
        print("Database connection closed.")