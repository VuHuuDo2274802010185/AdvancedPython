from flask import session, redirect, url_for, flash
from functools import wraps

def login_required(f):
    """Decorator để yêu cầu người dùng đăng nhập."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('Bạn cần đăng nhập để tiếp tục!', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function