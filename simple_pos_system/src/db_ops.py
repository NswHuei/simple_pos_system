import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'pos.db')

def insert_product(barcode, name, category, note):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO product (barcode, name, category, note, created_at, updated_at)
        VALUES (?, ?, ?, ?, datetime('now'), datetime('now'))
    """, (barcode, name, category, note))
    conn.commit()
    conn.close()

def insert_supplier_price(barcode, supplier, purchase_price):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO supplier_price (barcode, supplier, purchase_price, purchase_date)
        VALUES (?, ?, ?, datetime('now'))
    """, (barcode, supplier, purchase_price))
    conn.commit()
    conn.close()

def insert_sale(barcode, price, payment_method):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sales (barcode, price, datetime, payment_method)
        VALUES (?, ?, datetime('now'), ?)
    """, (barcode, price, payment_method))
    conn.commit()
    conn.close()