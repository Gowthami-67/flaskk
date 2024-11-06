import sqlite3

# Connect to SQLite database (this will create expense.db if it doesn't exist)
conn = sqlite3.connect('expense.db')
cursor = conn.cursor()

# Create the 'expenses' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT,
        date TEXT NOT NULL
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")