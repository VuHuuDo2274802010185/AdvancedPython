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
    app.run(debug=True, use_reloader=False)

def open_browser():
    """Mở trình duyệt web với URL ứng dụng."""
    time.sleep(1)  # Đảm bảo ứng dụng đã khởi động trước khi mở trình duyệt
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Tạo và bắt đầu luồng cho ứng dụng Flask
    threading.Thread(target=run_app).start()
    
    # Mở trình duyệt trong một luồng riêng
    threading.Thread(target=open_browser).start()

    # Giữ cho chương trình chạy liên tục
    while True:
        time.sleep(1)