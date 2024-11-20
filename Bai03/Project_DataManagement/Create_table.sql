-- Tạo cơ sở dữ liệu
CREATE DATABASE IF NOT EXISTS test;

-- Sử dụng cơ sở dữ liệu vừa tạo
USE test;

-- Tạo bảng danhsach
CREATE TABLE IF NOT EXISTS danhsach (
    id SERIAL PRIMARY KEY,
    hoten VARCHAR(100) NOT NULL,
    diachi VARCHAR(255) NOT NULL
);