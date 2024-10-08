import tkinter as tk
from tkinter import messagebox, ttk
from function import *

# Hàm thêm dữ liệu
def on_add_data():
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    
    if not name or not age.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid name and age (numeric).")
        return

    result = add_data(name, int(age))
    messagebox.showinfo("Result", result)
    display_data_output()  # Cập nhật dữ liệu ngay lập tức sau khi thêm

# Hàm xóa dữ liệu
def on_delete_data():
    id_to_delete = entry_id.get().strip()
    
    if not id_to_delete.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid numeric ID.")
        return

    result = delete_data(int(id_to_delete))
    messagebox.showinfo("Result", result)
    display_data_output()  # Cập nhật dữ liệu ngay lập tức sau khi xóa

# Hàm chỉnh sửa dữ liệu
def on_edit_data():
    id_to_edit = entry_edit_id.get().strip()
    new_name = entry_edit_name.get().strip()
    new_age = entry_edit_age.get().strip()
    
    if not id_to_edit.isdigit() or not new_name or not new_age.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid ID, name, and age (numeric).")
        return

    result = edit_data(int(id_to_edit), new_name, int(new_age))
    messagebox.showinfo("Result", result)
    display_data_output()  # Cập nhật dữ liệu ngay lập tức sau khi chỉnh sửa

# Hàm reset database
def on_reset_database():
    result = reset_database()
    messagebox.showinfo("Result", result)
    display_data_output()  # Cập nhật dữ liệu ngay lập tức sau khi reset

# Hàm hiển thị dữ liệu
def display_data_output():
    rows = display_data()
    text_output.delete('1.0', tk.END)  # Xóa nội dung cũ trong Text widget
    for row in rows:
        text_output.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}\n")

# Tạo giao diện GUI với tkinter
root = tk.Tk()
root.title("PostgreSQL Data Entry")
root.geometry("500x600")

# Tạo Notebook cho các tab
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Tạo tab thêm dữ liệu
tab_add = tk.Frame(notebook)
notebook.add(tab_add, text="Add Data")

label_name = tk.Label(tab_add, text="Name:")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(tab_add)
entry_name.grid(row=1, column=0, padx=5, pady=5)

label_age = tk.Label(tab_add, text="Age:")
label_age.grid(row=2, column=0, padx=5, pady=5)
entry_age = tk.Entry(tab_add)
entry_age.grid(row=3, column=0, padx=5, pady=5)

# Nút để thêm dữ liệu vào cơ sở dữ liệu
btn_add = tk.Button(tab_add, text="Add Data", command=on_add_data)
btn_add.grid(row=4, column=0, padx=5, pady=20)

# Tạo tab xóa dữ liệu
tab_delete = tk.Frame(notebook)
notebook.add(tab_delete, text="Delete Data")

label_id = tk.Label(tab_delete, text="ID to Delete:")
label_id.grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(tab_delete)
entry_id.grid(row=1, column=0, padx=5, pady=5)

# Nút để xóa dữ liệu theo ID
btn_delete = tk.Button(tab_delete, text="Delete Data", command=on_delete_data)
btn_delete.grid(row=2, column=0, padx=5, pady=20)

# Tạo tab chỉnh sửa dữ liệu
tab_edit = tk.Frame(notebook)
notebook.add(tab_edit, text="Edit Data")

label_edit_id = tk.Label(tab_edit, text="ID to Edit:")
label_edit_id.grid(row=0, column=0, padx=5, pady=5)
entry_edit_id = tk.Entry(tab_edit)
entry_edit_id.grid(row=1, column=0, padx=5, pady=5)

label_edit_name = tk.Label(tab_edit, text="New Name:")
label_edit_name.grid(row=2, column=0, padx=5, pady=5)
entry_edit_name = tk.Entry(tab_edit)
entry_edit_name.grid(row=3, column=0, padx=5, pady=5)

label_edit_age = tk.Label(tab_edit, text="New Age:")
label_edit_age.grid(row=4, column=0, padx=5, pady=5)
entry_edit_age = tk.Entry(tab_edit)
entry_edit_age.grid(row=5, column=0, padx=5, pady=5)

# Nút để chỉnh sửa dữ liệu theo ID
btn_edit = tk.Button(tab_edit, text="Edit Data", command=on_edit_data)
btn_edit.grid(row=6, column=0, padx=5, pady=20)

# Nút để reset toàn bộ dữ liệu
btn_reset = tk.Button(root, text="Reset Database", command=on_reset_database)
btn_reset.pack(pady=10)

# Text widget để hiển thị dữ liệu từ bảng
text_output = tk.Text(root, height=15, width=60)
text_output.pack(padx=10, pady=20)

# Hiển thị dữ liệu ban đầu khi khởi động chương trình
display_data_output()

root.mainloop()
