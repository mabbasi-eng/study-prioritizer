from flask import Flask, render_template
from database import init_db, get_all_tasks

# Create the Flask app
app = Flask(__name__)

# Create the database/table
init_db()


# This route controls the homepage
@app.route("/")
def index():
    tasks = get_all_tasks()
    return render_template("index.html", tasks=tasks)


# This starts the website when you run python app.py
if __name__ == "__main__":
    app.run(debug=True)