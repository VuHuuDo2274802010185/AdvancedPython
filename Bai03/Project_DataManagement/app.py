from flask import Flask
import threading
import time
import webbrowser
from config import app_config
from routes.main_routes import main_routes
from routes.crud_routes import crud_routes

app = Flask(__name__)
app.config.update(app_config)

# Đăng ký các blueprint cho route
app.register_blueprint(main_routes)
app.register_blueprint(crud_routes)

def run_app():
    """Chạy ứng dụng Flask."""
    try:
        app.run(debug=True, use_reloader=False)
    except Exception as e:
        print(f"Lỗi khi chạy ứng dụng Flask: {e}")

def open_browser():
    """Mở trình duyệt web với URL của ứng dụng."""
    time.sleep(1)  # Đảm bảo ứng dụng đã khởi động trước khi mở trình duyệt
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Tạo và bắt đầu luồng cho ứng dụng Flask
    flask_thread = threading.Thread(target=run_app)
    flask_thread.start()
    
    # Mở trình duyệt trong một luồng riêng
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.start()

    # Giữ cho luồng chính chạy liên tục
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Đang tắt ứng dụng.")