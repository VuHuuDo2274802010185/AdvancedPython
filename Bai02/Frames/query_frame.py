import tkinter as tk
from tkinter import messagebox

class QueryFrame:
    def __init__(self, root, app):
        """Khởi tạo QueryFrame cho ứng dụng."""
        self.app = app
        self.table_name = tk.StringVar(value='danhsach')
        self.search_term = tk.StringVar()
        self.create_widgets(root)

    def create_widgets(self, root):
        """Tạo các widget cho QueryFrame."""
        frame = tk.Frame(root)
        frame.pack(pady=10)

        # Ô nhập tên bảng
        tk.Label(frame, text="Table Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(frame, textvariable=self.table_name).grid(row=0, column=1, padx=5, pady=5)

        # Nút tải dữ liệu từ bảng
        tk.Button(frame, text="Load Data", command=self.load_data).grid(row=1, column=0, padx=5, pady=5)

        # Ô nhập từ khóa tìm kiếm và nút tìm kiếm
        tk.Label(frame, text="Search:").grid(row=1, column=1, padx=5, pady=5, sticky="e")
        tk.Entry(frame, textvariable=self.search_term).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(frame, text="Search", command=self.search_data).grid(row=1, column=3, padx=5, pady=5)

        # Text box để hiển thị dữ liệu từ bảng
        self.data_display = tk.Text(root, height=10, width=50)
        self.data_display.pack(pady=10)

    def load_data(self):
        """Tải dữ liệu từ bảng."""
        try:
            self.app.load_data(self.table_name.get())
            messagebox.showinfo("Success", "Data loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

    def search_data(self):
        """Tìm kiếm dữ liệu dựa trên từ khóa."""
        try:
            self.app.search_data(self.table_name.get(), self.search_term.get())
            messagebox.showinfo("Success", "Search completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to search data: {e}")

    def update_data_display(self, rows):
        """Cập nhật hiển thị dữ liệu."""
        self.data_display.delete(1.0, tk.END)
        if rows:
            for row in rows:
                self.data_display.insert(tk.END, f"{row}\n")
        else:
            self.data_display.insert(tk.END, "No data found.")
