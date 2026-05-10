import sqlite3

#name of database that stores all of the tasks
DATABASE = "tasks.db"


#This function connects to the database.
#Use it to 1. add tasks 2. get tasks 3. update tasks 4. delete tasks
def get_connection():
    conn = sqlite3.connect(DATABASE)

    #makes rows easier to use
    conn.row_factory = sqlite3.Row

    #send database connection back to function that needs it
    return conn 
    

#This function creates the tasks table.
#A table is like a spreadsheet.
#Each row is one task.
#Each column stores one piece of information about that task
def init_db():
    conn = get_connection() #open a connection to the database

    cursor = conn.cursor() #what sends commands to the database

    #a column looks like: name type rules
    #ex: title TEXT NOT NULL; means the title column stores text, and it can't be empty
    #1. id: unique number for each task; automatically goes up by 1
    #2. title: name of task
    #3. task_type: assignment, test, lab, quiz, or project
    #4. course: the class the task belongs to
    #5. due_date
    #6. estimated_hrs: how many hrs the task might take to finish
    #7. difficulty: how hard the task is on a scale of 1-5
    #8. importance: how important class/task is, scale of 1-5
    #9. completion: Percentage of task done
    #10. priority_score: final score calculated by priority.py file; higher tasks mean task should be worked on sooner.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT NOT NULL,
        task_type TEXT NOT NULL,
        course TEXT NOT NULL,
        due_date TEXT NOT NULL,
        estimated_hrs REAL NOT NULL CHECK (estimated_hrs >= 0),
        difficulty INTEGER NOT NULL CHECK (difficulty >= 1 AND difficulty <= 5),
        importance INTEGER NOT NULL CHECK (importance >= 1 AND importance <= 5),
        completion INTEGER NOT NULL DEFAULT 0 CHECK (completion >= 0 AND completion <= 100),
        priority_score REAL NOT NULL DEFAULT 0
        )
    """)

    # Save changes to database
    conn.commit()

    # Close connection
    conn.close()

#this function adds new task to database
def add_task(title, task_type, course, due_date, estimated_hrs, difficulty, importance, completion, priority_score):
    #open database
    conn = get_connection()

    #create a cursor to run SQL commands
    cursor = conn.cursor()

    #this SQL command inserts a new row
    #question marks are placeholders; get replace by the values in tuple.
    cursor.execute("""
        INSERT INTO tasks (
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
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        title,
        task_type,
        course,
        due_date,
        estimated_hrs,
        difficulty,
        importance,
        completion,
        priority_score
    ))
    #save the new task
    conn.commit()

    #close connection
    conn.close()

#This function gets every task from database
def get_all_tasks():
    # Open the database.
    conn = get_connection()

    # Create a cursor to run a SQL command.
    cursor = conn.cursor()

    # This gets all columns from all tasks.
    #
    # ORDER BY priority_score DESC means:
    #   show bigger priority scores first.
    #
    # due_date ASC means:
    #   if two tasks have the same priority score,
    #   show the one with the earlier due date first.
    cursor.execute("""
        SELECT * FROM tasks
        ORDER BY priority_score DESC, due_date ASC
    """)

    # Get all the rows from the result.
    tasks = cursor.fetchall()

    # Close the database connection.
    conn.close()

    # Send the tasks back to app.py.
    return tasks

#This function gets one task using its id. 
def get_task_by_id(task_id):
    # Open the database.
    conn = get_connection()

    # Create a cursor.
    cursor = conn.cursor()

    # Find the task where the id matches the task_id we were given.
    cursor.execute("""
        SELECT * FROM tasks
        WHERE id = ?
    """, (task_id,))

    # fetchone() gets one result instead of many results.
    task = cursor.fetchone()

    # Close the database.
    conn.close()

    # Send the task back.
    return task

#This functions marks a task as completed; also changes priority score to 0
def mark_task_complete(task_id):
    # Open the database.
    conn = get_connection()

    # Create a cursor.
    cursor = conn.cursor()

    # Update the task that has the matching id.
    cursor.execute("""
        UPDATE tasks
        SET completion = 100,
            priority_score = 0
        WHERE id = ?
    """, (task_id,))

    # Save the update.
    conn.commit()

    # Close the database.
    conn.close()

#This function updates the percentage of completion of a task
def update_task_completion(task_id, completion, priority_score):
    # Open the database.
    conn = get_connection()

    # Create a cursor.
    cursor = conn.cursor()

    # Update completion and priority_score for the matching task.
    cursor.execute("""
        UPDATE tasks
        SET completion = ?,
            priority_score = ?
        WHERE id = ?
    """, (completion, priority_score, task_id))

    # Save the changes.
    conn.commit()

    # Close the database.
    conn.close()

#This function deletes one task from database using its id.
def delete_task(task_id):
    # Open the database.
    conn = get_connection()

    # Create a cursor.
    cursor = conn.cursor()

    # Delete the task where the id matches the task_id.
    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))

    # Save the delete.
    conn.commit()

    # Close the database.
    conn.close()