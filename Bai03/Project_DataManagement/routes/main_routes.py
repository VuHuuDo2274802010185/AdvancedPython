from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from database import get_db_connection
from decorators import login_required

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
@login_required
def index():
    """Hiển thị trang chính với danh sách từ cơ sở dữ liệu."""
    conn = get_db_connection()
    rows = []
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM danhsach')
                rows = cur.fetchall()
        except Exception as e:
            flash(f'Database query error: {e}', 'danger')
        finally:
            conn.close()
    else:
        flash('Không thể kết nối đến cơ sở dữ liệu.', 'danger')
    return render_template('index.html', rows=rows)

@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    """Xử lý đăng nhập người dùng."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Cần cập nhật xác thực thật
        if username == 'admin' and password == '1234':  
            session['logged_in'] = True
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('main_routes.index'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không đúng!', 'danger')
    
    return render_template('login.html')

@main_routes.route('/logout')
@login_required
def logout():
    """Xử lý đăng xuất người dùng."""
    session.pop('logged_in', None)
    flash('Bạn đã đăng xuất thành công!', 'success')
    return redirect(url_for('main_routes.login'))