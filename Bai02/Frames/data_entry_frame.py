import tkinter as tk
from tkinter import messagebox

class DataEntryFrame:
    def __init__(self, insert_frame, edit_frame, delete_frame, reset_frame, app):
        """Khởi tạo các tab nhập dữ liệu cho ứng dụng."""
        self.app = app
        self.table_name = app.query_frame.table_name  # Sử dụng cùng table_name với QueryFrame
        self.column1 = tk.StringVar()
        self.column2 = tk.StringVar()
        self.selected_id = tk.StringVar()

        # Khởi tạo các khung nhập liệu cho các tab khác nhau
        self.create_insert_tab(insert_frame)
        self.create_edit_tab(edit_frame)
        self.create_delete_tab(delete_frame)
        self.create_reset_tab(reset_frame)

    def create_insert_tab(self, frame):
        """Tạo tab nhập liệu."""
        self.create_label_entry(frame, "Ho ten:", self.column1, 0)
        self.create_label_entry(frame, "Dia chi:", self.column2, 1)

        tk.Button(frame, text="Insert Data", command=self.insert_data).grid(row=2, columnspan=2, pady=10)

    def create_edit_tab(self, frame):
        """Tạo tab chỉnh sửa dữ liệu."""
        self.create_label_entry(frame, "ID:", self.selected_id, 0)
        self.create_label_entry(frame, "Ho ten:", self.column1, 1)
        self.create_label_entry(frame, "Dia chi:", self.column2, 2)

        tk.Button(frame, text="Edit Data", command=self.edit_data).grid(row=3, columnspan=2, pady=10)

    def create_delete_tab(self, frame):
        """Tạo tab xóa dữ liệu."""
        self.create_label_entry(frame, "ID:", self.selected_id, 0)
        tk.Button(frame, text="Delete Data", command=self.delete_data).grid(row=1, columnspan=2, pady=10)

    def create_reset_tab(self, frame):
        """Tạo tab đặt lại dữ liệu."""
        tk.Button(frame, text="Reset Data", command=self.reset_data).grid(row=0, columnspan=2, pady=10)

    def create_label_entry(self, parent, label_text, variable, row):
        """Tạo nhãn và trường nhập liệu."""
        tk.Label(parent, text=label_text).grid(row=row, column=0, padx=5, pady=5, sticky="e")
        tk.Entry(parent, textvariable=variable).grid(row=row, column=1, padx=5, pady=5)

    def insert_data(self):
        """Chèn dữ liệu vào cơ sở dữ liệu."""
        if not self.column1.get() or not self.column2.get():
            messagebox.showerror("Error", "Please fill in all fields to insert data.")
            return
        self.app.insert_data(self.table_name.get(), self.column1.get(), self.column2.get())
        messagebox.showinfo("Success", "Data inserted successfully!")
        self.clear_inputs()

    def edit_data(self):
        """Chỉnh sửa dữ liệu trong cơ sở dữ liệu."""
        if not self.selected_id.get():
            messagebox.showerror("Error", "Please provide an ID to edit.")
            return
        if not self.column1.get() or not self.column2.get():
            messagebox.showerror("Error", "Please fill in all fields to edit data.")
            return
        self.app.edit_data(self.table_name.get(), self.column1.get(), self.column2.get(), self.selected_id.get())
        messagebox.showinfo("Success", "Data edited successfully!")
        self.clear_inputs()

    def delete_data(self):
        """Xóa dữ liệu khỏi cơ sở dữ liệu."""
        if not self.selected_id.get():
            messagebox.showerror("Error", "Please provide an ID to delete.")
            return
        self.app.delete_data(self.table_name.get(), self.selected_id.get())
        messagebox.showinfo("Success", "Data deleted successfully!")
        self.clear_inputs()

    def reset_data(self):
        """Đặt lại dữ liệu trong cơ sở dữ liệu."""
        self.app.reset_data(self.table_name.get())
        messagebox.showinfo("Success", "Data reset successfully!")
        self.clear_inputs()

    def clear_inputs(self):
        """Xóa tất cả các trường nhập liệu."""
        self.column1.set("")
        self.column2.set("")
        self.selected_id.set("")
