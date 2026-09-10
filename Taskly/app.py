from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.db")

def init_db():
    connection = sqlite3.connect(DATABASE)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()

@app.route("/api/tasks", methods=["POST"])
def add_task():

    data = request.get_json()

    title = data["title"]

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (title,)
    )

    connection.commit()

    task_id = cursor.lastrowid

    connection.close()

    return jsonify({
        "id": task_id,
        "title": title,
        "completed": 0
    })

@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/tasks")
def tasks():
    return render_template("tasks.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)