from flask import Flask, render_template
import crawlTasks

app = Flask(__name__)

tasks = crawlTasks.get_tasks()
print(tasks)


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    app.run(debug=True)
