
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = [
    {"id": 1, "name": "Rahul", "course": "Computer Engineering"},
    {"id": 2, "name": "Priya", "course": "Information Technology"}
]

@app.route("/")
def home():
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    name = request.form.get("name", "").strip()
    course = request.form.get("course", "").strip()

    if name and course:
        new_id = max((s["id"] for s in students), default=0) + 1
        students.append({
            "id": new_id,
            "name": name,
            "course": course
        })

    return redirect(url_for("home"))

@app.route("/api/students", methods=["GET"])
def get_students():
    return {"students": students}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
