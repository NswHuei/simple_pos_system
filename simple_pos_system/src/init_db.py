import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # main.py 所在目录
PROJECT_ROOT = os.path.dirname(BASE_DIR)  # 假设 main.py 在 src/ 下

def init_db():
    db_path = os.path.join(PROJECT_ROOT, 'data', 'pos.db')
    sql_path = os.path.join(PROJECT_ROOT, 'sql', 'init.sql')

    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    with open(sql_path, 'r', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
