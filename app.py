from flask import Flask, render_template, request, redirect
from database import (
    init_db,
    add_task,
    get_tasks,
    delete_task,
    get_task,
    update_task
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        title = request.form["title"]

        if title.strip():
            add_task(title)

        return redirect("/")

    tasks = get_tasks()

    return render_template(
        "index.html",
        tasks=tasks
    )


@app.route("/delete/<int:task_id>")
def delete(task_id):

    delete_task(task_id)

    return redirect("/")


@app.route("/update/<int:task_id>", methods=["GET", "POST"])
def update(task_id):

    if request.method == "POST":

        title = request.form["title"]

        update_task(task_id, title)

        return redirect("/")

    task = get_task(task_id)

    return render_template(
        "updates.html",
        task=task
    )


if __name__ == "__main__":

    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)
