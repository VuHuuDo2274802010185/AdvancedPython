import tkinter as tk
from tkinter import messagebox

class ConnectionFrame:
    def __init__(self, root, app):
        """Khởi tạo khung kết nối đến cơ sở dữ liệu."""
        self.app = app
        self.db_name = tk.StringVar(value='test')
        self.user = tk.StringVar(value='postgres')
        self.password = tk.StringVar(value='Do12345678910..')
        self.host = tk.StringVar(value='localhost')
        self.port = tk.StringVar(value='5555')

        self.create_widgets(root)

    def create_widgets(self, root):
        """Tạo các widget cho khung kết nối."""
        connection_frame = tk.Frame(root)
        connection_frame.pack(pady=10)

        # Tạo các trường nhập liệu bằng cách gọi phương thức tạo nhãn và trường nhập
        self.create_label_entry(connection_frame, "DB Name:", self.db_name, 0)
        self.create_label_entry(connection_frame, "User:", self.user, 1)
        self.create_label_entry(connection_frame, "Password:", self.password, 2, show="*")
        self.create_label_entry(connection_frame, "Host:", self.host, 3)
        self.create_label_entry(connection_frame, "Port:", self.port, 4)

        # Nút kết nối
        tk.Button(connection_frame, text="Connect", command=self.connect_db).grid(row=5, columnspan=2, pady=10)

    def create_label_entry(self, parent, label_text, variable, row, show=None):
        """Tạo nhãn và trường nhập liệu."""
        tk.Label(parent, text=label_text).grid(row=row, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(parent, textvariable=variable, show=show).grid(row=row, column=1, padx=5, pady=5)

    def connect_db(self):
        """Kết nối đến cơ sở dữ liệu và thông báo lỗi nếu có."""
        db_name = self.db_name.get()
        user = self.user.get()
        password = self.password.get()
        host = self.host.get()
        port = self.port.get()

        # Kiểm tra xem tất cả các trường đều được điền
        if not all([db_name, user, password, host, port]):
            messagebox.showwarning("Input Error", "Vui lòng điền đầy đủ thông tin kết nối.")
            return

        try:
            self.app.connect_db(db_name, user, password, host, port)
            messagebox.showinfo("Success", "Kết nối thành công!")
        except Exception as e:
            messagebox.showerror("Connection Error", f"Kết nối không thành công: {e}")
