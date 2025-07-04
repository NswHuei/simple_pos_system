-- 创建 product 表
CREATE TABLE IF NOT EXISTS product (
    barcode TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    note TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

-- 创建 supplier_price 表
CREATE TABLE IF NOT EXISTS supplier_price (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    barcode TEXT NOT NULL,
    supplier TEXT NOT NULL,
    purchase_price REAL NOT NULL,
    purchase_date TEXT NOT NULL,
    FOREIGN KEY (barcode) REFERENCES product(barcode)
);

-- 创建 sales 表
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    barcode TEXT NOT NULL,
    price REAL NOT NULL,
    datetime TEXT NOT NULL,
    payment_method TEXT NOT NULL,
    FOREIGN KEY (barcode) REFERENCES product(barcode)
);



-- 插入几条商品
INSERT INTO product (barcode, name, category, note, created_at, updated_at)
VALUES 
('1234567890123', '可乐 500ml', '饮料', 'Coca-Cola 500ml', datetime('now'), datetime('now')),
('9876543210987', '薯片 100g', '零食', 'Lays Chips 100g', datetime('now'), datetime('now'));

-- 插入进货记录
INSERT INTO supplier_price (barcode, supplier, purchase_price, purchase_date)
VALUES 
('1234567890123', 'Supplier A', 0.5, datetime('now')),
('9876543210987', 'Supplier B', 0.8, datetime('now'));

-- 插入销售记录
INSERT INTO sales (barcode, price, datetime, payment_method)
VALUES 
('1234567890123', 1.0, datetime('now'), 'cash'),
('9876543210987', 1.5, datetime('now'), 'card');
