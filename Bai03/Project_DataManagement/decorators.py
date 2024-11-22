from flask import session, redirect, url_for, flash
from functools import wraps

def login_required(f):
    """Decorator để yêu cầu người dùng đăng nhập."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Kiểm tra xem người dùng đã đăng nhập hay chưa
        if 'logged_in' not in session:
            flash('Bạn cần đăng nhập để tiếp tục!', 'warning')
            return redirect(url_for('main_routes.login'))  # Chuyển hướng đến trang đăng nhập
        return f(*args, **kwargs)  # Gọi hàm mục tiêu nếu đã đăng nhập
    return decorated_function