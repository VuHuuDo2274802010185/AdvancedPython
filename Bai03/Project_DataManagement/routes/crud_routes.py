from flask import Blueprint, request, redirect, url_for, flash, render_template
from database import get_db_connection
from decorators import login_required

crud_routes = Blueprint('crud_routes', __name__)

@crud_routes.route('/insert', methods=['POST'])
@login_required
def insert():
    """Thêm một bản ghi mới vào cơ sở dữ liệu."""
    hoten = request.form.get('hoten')
    diachi = request.form.get('diachi')
    
    if not hoten or not diachi:
        flash('Họ tên và địa chỉ không được để trống!', 'danger')
        return redirect(url_for('main_routes.index'))
    
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO danhsach (hoten, diachi) VALUES (%s, %s)', (hoten, diachi))
            conn.commit()
            flash('Thêm dữ liệu thành công!', 'success')
        except Exception as e:
            flash(f'Lỗi khi thêm dữ liệu: {e}', 'danger')
        finally:
            conn.close()
    else:
        flash('Không thể kết nối đến cơ sở dữ liệu.', 'danger')
    
    return redirect(url_for('main_routes.index'))

@crud_routes.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    """Xóa một bản ghi khỏi cơ sở dữ liệu."""
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute('DELETE FROM danhsach WHERE id = %s', (id,))
            conn.commit()
            flash('Xóa dữ liệu thành công!', 'success')
        except Exception as e:
            flash(f'Lỗi khi xóa dữ liệu: {e}', 'danger')
        finally:
            conn.close()
    else:
        flash('Không thể kết nối đến cơ sở dữ liệu.', 'danger')
    
    return redirect(url_for('main_routes.index'))

@crud_routes.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    """Chỉnh sửa một bản ghi trong cơ sở dữ liệu."""
    conn = get_db_connection()
    row = None
    if conn:
        try:
            if request.method == 'POST':
                hoten = request.form.get('hoten')
                diachi = request.form.get('diachi')
                if not hoten or not diachi:
                    flash('Họ tên và địa chỉ không được để trống!', 'danger')
                    return redirect(url_for('crud_routes.edit', id=id))
                with conn.cursor() as cur:
                    cur.execute('UPDATE danhsach SET hoten = %s, diachi = %s WHERE id = %s', (hoten, diachi, id))
                conn.commit()
                flash('Cập nhật dữ liệu thành công!', 'success')
                return redirect(url_for('main_routes.index'))
            
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM danhsach WHERE id = %s', (id,))
                row = cur.fetchone()
        except Exception as e:
            flash(f'Lỗi khi lấy dữ liệu: {e}', 'danger')
        finally:
            conn.close()
    else:
        flash('Không thể kết nối đến cơ sở dữ liệu.', 'danger')
    
    return render_template('edit.html', row=row)

@crud_routes.route('/reset', methods=['POST'])
@login_required
def reset_database():
    """Đặt lại cơ sở dữ liệu."""
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute('DROP TABLE IF EXISTS danhsach;')
                cur.execute('CREATE TABLE danhsach (id SERIAL PRIMARY KEY, hoten VARCHAR(100), diachi VARCHAR(255));')
            conn.commit()
            flash('Cơ sở dữ liệu đã được đặt lại thành công!', 'success')
        except Exception as e:
            flash(f'Lỗi khi đặt lại cơ sở dữ liệu: {e}', 'danger')
        finally:
            conn.close()
    else:
        flash('Không thể kết nối đến cơ sở dữ liệu.', 'danger')
    
    return redirect(url_for('main_routes.index'))