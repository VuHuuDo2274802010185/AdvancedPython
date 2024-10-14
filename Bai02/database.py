import psycopg2
from psycopg2 import sql

class DatabaseManager:
    def __init__(self, db_name, user, password, host, port):
        """Khởi tạo DatabaseManager với thông tin kết nối."""
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.cur = None

    def connect(self):
        """Kết nối đến cơ sở dữ liệu PostgreSQL."""
        if self.conn is not None:
            raise ConnectionError("Connection already established.")
        
        try:
            self.conn = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cur = self.conn.cursor()
        except psycopg2.Error as e:
            raise ConnectionError(f"Error connecting to the database: {e}")

    def fetch_data(self, query, params=None):
        """Lấy dữ liệu từ cơ sở dữ liệu."""
        self._check_connection()
        try:
            self.cur.execute(query, params)
            return self.cur.fetchall()
        except psycopg2.Error as e:
            raise RuntimeError(f"Error fetching data: {e}")

    def execute_query(self, query, params=None):
        """Thực hiện một truy vấn (INSERT, UPDATE, DELETE)."""
        self._check_connection()
        try:
            self.cur.execute(query, params)
            self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            raise RuntimeError(f"Error executing query: {e}")

    def close(self):
        """Đóng kết nối và con trỏ cơ sở dữ liệu."""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
            self.conn = None

    def _check_connection(self):
        """Kiểm tra kết nối trước khi thực hiện truy vấn."""
        if self.conn is None:
            raise ConnectionError("Database connection is not established. Please connect first.")

    def get_cursor(self):
        """Trả về con trỏ hiện tại."""
        self._check_connection()
        return self.cur

# Sử dụng sql.SQL và sql.Identifier để tạo truy vấn an toàn hơn
def create_safe_query(table_name, column_name, value):
    query = sql.SQL("SELECT * FROM {} WHERE {} = %s").format(
        sql.Identifier(table_name),
        sql.Identifier(column_name)
    )
    return query, (value,)
