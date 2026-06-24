import sqlite3

conn = sqlite3.connect('employee.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT
)
''')

employees = [
    (1, 'John'),
    (2, 'Mary'),
    (3, 'Sam'),
    (4, 'David'),
    (5, 'Chris')
]

cursor.executemany(
    'INSERT OR REPLACE INTO employees VALUES (?, ?)',
    employees
)

conn.commit()
conn.close()

print("Database created successfully")