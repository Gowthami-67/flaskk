from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL
        )
   ''')
    conn.commit()
    conn.close()

init_db()

# Route for homepage
@app.route('/')
def index():
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    expenses = cursor.fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)

# Add new expense
@app.route('/add', methods=['POST'])
def add_expense():
    description = request.form['description']
    amount = float(request.form['amount'])
    category = request.form['category']
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO expenses (description, amount, category) VALUES (?, ?, ?)', (description, amount, category))
    conn.commit()
    conn.close()
    return redirect('/')

# Delete expense
@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()
    return redirect('/')

# Endpoint for fetching chart data
@app.route('/chart-data')
def chart_data():
    conn = sqlite3.connect('expense.db')
    cursor = conn.cursor()
    cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)