-- Create the users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Insert a sample user (username: admin, password: admin123)
INSERT INTO users (username, password_hash) 
VALUES ('admin', crypt('admin123', gen_salt('bf')));

SELECT * FROM users;
