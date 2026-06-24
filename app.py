from flask import Flask
import sqlite3
import os

from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "Employee App Working"

@app.route("/employees")
def employees():

    db_path = os.path.join(os.path.dirname(__file__), "employee.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()

    conn.close()

    html = "<h2>Employee List</h2><table border='1'>"
    html += "<tr><th>ID</th><th>Name</th></tr>"

    for emp in data:
        html += f"<tr><td>{emp[0]}</td><td>{emp[1]}</td></tr>"

    html += "</table>"

    return html



@app.route("/add")
def add_employee():

    db_path = os.path.join(os.path.dirname(__file__), "employee.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employees (name) VALUES ('New Employee')"
    )

    conn.commit()
    conn.close()

    return "Employee Added Successfully"
app.run(host="0.0.0.0", port=5000)