#Flask creates web app
#render template shows an HTML file from templates folder
#request lets flask read info from a form
#redirect sends user to another page
#url_for builds a correct route URL for a function 
from flask import Flask, render_template, request, redirect, url_for

#imports database functions
from database import (
    init_db,
    add_task,
    get_all_tasks,
    mark_task_complete,
    delete_task
)
#imports priority calculator
from priority import calculate_priority #whenever user adds a task, Flask will send info to this function and calculate score

app = Flask(__name__) #create Flask app

#Set up database when app starts
init_db()

#This route controls homepage. '/' means the main page of website
#Ex. http://127.0.0.1:5000/
@app.route("/")
def index():
    #Get every task 
    tasks = get_all_tasks()

    #show index.html and send task list to index.html
    return render_template("index.html", tasks=tasks)

# This route controls the add task page.
# "/add" means the page where users can add a new task.
#
# methods=["GET", "POST"] means this page can do two things:
# GET = show the blank form
# POST = receive the form after the user submits it
@app.route("/add", methods=["GET", "POST"])
def add():
    # Check if the user submitted the form.
    # When a form is submitted, the request method is POST.
    if request.method == "POST":

        # Get the title from the form.
        # This matches an HTML input with name="title".
        title = request.form["title"]

        # Get the task type from the form.
        # Example: Assignment, Test, Quiz, Project, Lab
        task_type = request.form["task_type"]

        # Get the course name from the form.
        # Example: Math, English, Biology
        course = request.form["course"]

        # Get the due date from the form.
        # The date will usually look like "2026-05-10".
        due_date = request.form["due_date"]

        # Get the estimated hours from the form.
        # Form data comes in as text, so we convert it to a float.
        # A float allows decimals like 1.5 or 2.5.
        estimated_hrs = float(request.form["estimated_hrs"])

        # Get the difficulty from the form.
        # Convert it to an integer because it should be a whole number from 1 to 5.
        difficulty = int(request.form["difficulty"])

        # Get the importance from the form.
        # Convert it to an integer because it should be a whole number from 1 to 5.
        importance = int(request.form["importance"])

        # Get the completion percentage from the form.
        # Convert it to an integer because it should be a whole number from 0 to 100.
        completion = int(request.form["completion"])

        # Calculate the priority score using the function from priority.py.
        # We send in the task details.
        # The function returns a number.
        priority_score = calculate_priority(
            due_date,
            estimated_hrs,
            difficulty,
            importance,
            completion
        )

        # Save the new task into the database.
        # This uses the add_task() function from database.py.
        add_task(
            title,
            task_type,
            course,
            due_date,
            estimated_hrs,
            difficulty,
            importance,
            completion,
            priority_score
        )

        # After saving the task, send the user back to the homepage.
        # url_for("index") finds the route for the index() function.
        return redirect(url_for("index"))

    # If the user has NOT submitted the form yet,
    # show them the add_task.html page.
    #
    # This happens when they first visit /add.
    return render_template("add_task.html")


# This route marks a task as complete.
#
# <int:task_id> means the URL will contain a task id number.
# Example:
# /complete/3
#
# In that example, task_id would be 3.
#
# methods=["POST"] means this route should be used by a form button,
# not just by typing the URL into the browser.
@app.route("/complete/<int:task_id>", methods=["POST"])
def complete(task_id):
    # Mark the task as complete in the database.
    # This sets completion to 100 and priority_score to 0.
    mark_task_complete(task_id)

    # After updating the task, send the user back to the homepage.
    return redirect(url_for("index"))


# This route deletes a task.
#
# <int:task_id> means the URL will contain the id of the task to delete.
# Example:
# /delete/5
#
# In that example, task_id would be 5.
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    # Delete the task from the database.
    delete_task(task_id)

    # After deleting the task, send the user back to the homepage.
    return redirect(url_for("index"))


# This checks if we are running this file directly.
# If we run "python app.py", this will be true.
if __name__ == "__main__":

    # Start the Flask development server.
    #
    # debug=True helps while coding because:
    # 1. It shows detailed error messages.
    # 2. It reloads the app when you save changes.
    #
    # Do not use debug=True for a real public website,
    # but it is perfect for a school/local project.
    app.run(debug=True)