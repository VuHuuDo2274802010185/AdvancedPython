import tkinter as tk
from tkinter import ttk
from Frames.connection_frame import ConnectionFrame
from Frames.query_frame import QueryFrame
from Frames.data_entry_frame import DataEntryFrame
from database import DatabaseManager

class DatabaseApp:
    def __init__(self, root):
        """Khởi tạo ứng dụng Database."""
        self.root = root
        self.root.title("Database App")

        # Biến quản lý kết nối cơ sở dữ liệu
        self.db_manager = None

        # Tạo các khung chức năng
        self.connection_frame = ConnectionFrame(self.root, self)
        self.query_frame = QueryFrame(self.root, self)

        # Tạo Notebook để chứa các tab
        self.create_notebook()

    def create_notebook(self):
        """Tạo Notebook để chứa các tab nhập liệu."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, fill='both', expand=True)

        # Danh sách tên tab và khung tương ứng
        tabs = ["Insert Data", "Edit Data", "Delete Data", "Reset Data"]
        self.frames = {}

        for tab in tabs:
            frame = tk.Frame(self.notebook)
            self.notebook.add(frame, text=tab)
            self.frames[tab] = frame

        # Khởi tạo các khung nhập liệu cho từng tab
        self.data_entry_frame = DataEntryFrame(self.frames["Insert Data"], self.frames["Edit Data"],
                                               self.frames["Delete Data"], self.frames["Reset Data"], self)

    def connect_db(self, db_name, user, password, host, port):
        """Kết nối đến cơ sở dữ liệu."""
        try:
            self.db_manager = DatabaseManager(db_name, user, password, host, port)
            self.db_manager.connect()
        except Exception as e:
            print(f"Không thể kết nối đến cơ sở dữ liệu: {e}")

    def load_data(self, table_name):
        """Tải dữ liệu từ bảng vào giao diện."""
        query = f"SELECT * FROM {table_name}"
        rows = self.db_manager.fetch_data(query)
        self.query_frame.update_data_display(rows)

    def insert_data(self, table_name, column1, column2):
        """Chèn dữ liệu vào bảng."""
        insert_query = f"INSERT INTO {table_name} (hoten, diachi) VALUES (%s, %s)"
        data_to_insert = (column1, column2)
        self._execute_query(insert_query, data_to_insert)

    def edit_data(self, table_name, column1, column2, selected_id):
        """Chỉnh sửa dữ liệu trong bảng."""
        update_query = f"UPDATE {table_name} SET hoten = %s, diachi = %s WHERE id = %s"
        self._execute_query(update_query, (column1, column2, selected_id))

    def delete_data(self, table_name, selected_id):
        """Xóa dữ liệu khỏi bảng."""
        delete_query = f"DELETE FROM {table_name} WHERE id = %s"
        self._execute_query(delete_query, (selected_id,))

    def reset_data(self, table_name):
        """Xóa toàn bộ dữ liệu và đặt lại sequence ID."""
        delete_all_query = f"DELETE FROM {table_name}"
        reset_sequence_query = f"ALTER SEQUENCE {table_name}_id_seq RESTART WITH 1"
        self._execute_query(delete_all_query)
        self._execute_query(reset_sequence_query)
        self.load_data(table_name)

    def search_data(self, table_name, search_term):
        """Tìm kiếm dữ liệu dựa trên từ khóa."""
        search_query = f"""
            SELECT * FROM {table_name}
            WHERE hoten ILIKE %s OR diachi ILIKE %s
        """
        search_pattern = f"%{search_term}%"
        rows = self.db_manager.fetch_data(search_query, (search_pattern, search_pattern))
        self.query_frame.update_data_display(rows)

    def _execute_query(self, query, params=None):
        """Thực thi truy vấn với quản lý lỗi."""
        try:
            self.db_manager.execute_query(query, params)
        except Exception as e:
            print(f"Đã xảy ra lỗi khi thực thi truy vấn: {e}")
