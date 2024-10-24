import sqlite3
import os
import logging
from datetime import datetime

def create_database():
    for folder in ['data', 'logs']:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tables_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_name TEXT,
        columns_info TEXT,
        sample_data TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS query_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        natural_query TEXT,
        generated_sql TEXT,
        execution_result TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS error_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        error_type TEXT,
        query TEXT,
        message TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS query_metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query_id INTEGER,
        execution_time REAL,
        row_count INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (query_id) REFERENCES query_history(id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        stock INTEGER
    )
    ''')
    
    cursor.execute('''
    INSERT OR IGNORE INTO tables_info (table_name, columns_info, sample_data)
    VALUES (
        'products',
        'id: INTEGER, name: TEXT, price: REAL, stock: INTEGER',
        'Sample: (1, "Laptop", 999.99, 50)'
    )
    ''')
    
    cursor.execute('''
    INSERT OR IGNORE INTO products (name, price, stock) VALUES 
        ("Laptop", 999.99, 50),
        ("Smartphone", 599.99, 100),
        ("Tablet", 299.99, 15),
        ("Headphones", 99.99, 200),
        ("Mouse", 29.99, 150)
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()