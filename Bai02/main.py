import tkinter as tk
from gui import DatabaseApp

def run_app():
    """Khởi tạo và chạy ứng dụng DatabaseApp."""
    root = tk.Tk()  # Khởi tạo cửa sổ Tkinter
    app = DatabaseApp(root)  # Tạo một instance của DatabaseApp
    root.mainloop()  # Chạy vòng lặp chính của ứng dụng

if __name__ == "__main__":
    try:
        run_app()  # Gọi hàm để chạy ứng dụng
    except Exception as e:
        print(f"Đã xảy ra lỗi khi khởi động ứng dụng: {e}")  # In ra thông báo lỗi
