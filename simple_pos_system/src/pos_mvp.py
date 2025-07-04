import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os
import csv

# 获取数据库路径
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "pos.db"))

# 查询全部数据
def fetch_data():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product")
        rows = cursor.fetchall()
        conn.close()

        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
    except Exception as e:
        messagebox.showerror("错误", f"查询失败：{e}")

# 模糊搜索
def search_data():
    keyword = search_var.get()
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product WHERE barcode LIKE ? OR name LIKE ? OR note LIKE ?", 
                    (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
        rows = cursor.fetchall()
        conn.close()

        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert("", "end", values=row)
    except Exception as e:
        messagebox.showerror("错误", f"查询失败：{e}")

# 导出 CSV
def export_to_csv():
    try:
        with open("export.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            for item in tree.get_children():
                writer.writerow(tree.item(item)['values'])
        messagebox.showinfo("成功", "已导出为 export.csv")
    except Exception as e:
        messagebox.showerror("错误", f"导出失败：{e}")

# 插入数据
def open_add_window():
    add_window = tk.Toplevel(root)
    add_window.title("添加商品")
    add_window.geometry("400x300")

    # 字段变量
    barcode_var = tk.StringVar()
    name_var = tk.StringVar()
    category_var = tk.StringVar()
    note_var = tk.StringVar()

    # 标签和输入框
    tk.Label(add_window, text="条形码:").pack()
    tk.Entry(add_window, textvariable=barcode_var).pack()

    tk.Label(add_window, text="商品名称:").pack()
    tk.Entry(add_window, textvariable=name_var).pack()

    tk.Label(add_window, text="分类:").pack()
    tk.Entry(add_window, textvariable=category_var).pack()

    tk.Label(add_window, text="备注:").pack()
    tk.Entry(add_window, textvariable=note_var).pack()

    # 保存按钮
    def save_product():
        barcode = barcode_var.get().strip()
        name = name_var.get().strip()
        category = category_var.get().strip()
        note = note_var.get().strip()

        if not barcode or not name:
            messagebox.showerror("错误", "条形码和商品名称为必填")
            return

        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO product (barcode, name, category, note, created_at, updated_at)
                VALUES (?, ?, ?, ?, datetime('now'), datetime('now'))
            """, (barcode, name, category, note))
            conn.commit()
            conn.close()

            messagebox.showinfo("成功", "商品添加成功！")
            add_window.destroy()
            fetch_data()  # 刷新主表
        except Exception as e:
            messagebox.showerror("错误", f"保存失败：{e}")

    tk.Button(add_window, text="保存", command=save_product).pack(pady=10)


# 创建主窗口
root = tk.Tk()
root.title("POS 数据查看器")
root.geometry("900x500")

# ===================== 控制区（搜索 + 按钮） =====================
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

search_var = tk.StringVar()
search_entry = tk.Entry(control_frame, textvariable=search_var, width=30)
search_entry.grid(row=0, column=0, padx=5)

btn_search = tk.Button(control_frame, text="搜索", command=search_data)
btn_search.grid(row=0, column=1, padx=5)

btn_view = tk.Button(control_frame, text="查看全部", command=fetch_data)
btn_view.grid(row=0, column=2, padx=5)

btn_export = tk.Button(control_frame, text="导出 CSV", command=export_to_csv)
btn_export.grid(row=0, column=3, padx=5)

btn_add = tk.Button(control_frame, text="添加商品", command=lambda: open_add_window())
btn_add.grid(row=0, column=4, padx=5)


# ===================== 表格区 =====================
table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

columns = ("barcode", "name", "category", "note", "created_at", "updated_at")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")

# 设置列头
tree.heading("barcode", text="条形码")
tree.heading("name", text="商品")
tree.heading("category", text="分类")
tree.heading("note", text="备注")
tree.heading("created_at", text="创建时间")
tree.heading("updated_at", text="更新时间")

# 设置列宽
for col in columns:
    tree.column(col, width=120, anchor="center")

# 添加滚动条
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree.pack(fill=tk.BOTH, expand=True)

# 启动时自动加载数据
fetch_data()

# 主循环
root.mainloop()
