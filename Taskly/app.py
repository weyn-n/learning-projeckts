from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "task.db")

print("DATABASE:", DATABASE)
print("EXISTS:", os.path.exists(DATABASE))

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

@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def complete_task(task_id):

    data = request.get_json()
    completed = data["completed"]

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE tasks SET completed = ? WHERE id = ?",
        (completed, task_id)
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Task updated"
    })

@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Task deleted"
    })


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    print("DATABASE:", DATABASE)

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    connection.close()

    return jsonify(tasks)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        print(username)
        print(password)

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        print(username)
        print(password)

    return render_template("login.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)