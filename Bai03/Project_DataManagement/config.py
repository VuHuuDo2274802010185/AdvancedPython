import os
from dotenv import load_dotenv

# Tải các biến môi trường từ file .env
load_dotenv()

# Cấu hình ứng dụng Flask
app_config = {
    'SECRET_KEY': os.getenv('SECRET_KEY', 'default_secret_key')
}

# Cấu hình cơ sở dữ liệu
DATABASE = {
    'dbname': os.getenv('DB_NAME', 'test'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'your_password'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5555')
}

def get_database_uri():
    """Tạo URI kết nối cơ sở dữ liệu."""
    return f"postgresql://{DATABASE['user']}:{DATABASE['password']}@" \
           f"{DATABASE['host']}:{DATABASE['port']}/{DATABASE['dbname']}"

# Ví dụ cách sử dụng
if __name__ == '__main__':
    print(f"Database URI: {get_database_uri()}")