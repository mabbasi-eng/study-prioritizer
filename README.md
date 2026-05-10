# StudyPrioritizer

StudyPrioritizer is a Flask web app that helps students decide which school task they should work on first.

Students can add assignments, tests, labs, quizzes, projects, and other academic tasks. The app stores each task in a local SQLite database and calculates a priority score based on due date, estimated time needed, difficulty, course importance, and completion percentage.

The goal of this project is to create a simple, useful productivity tool for students who want a clearer way to manage their academic workload.

---

## Features

- Add academic tasks
- Store tasks in a local SQLite database
- Automatically calculate task priority
- Rank tasks from highest priority to lowest priority
- View all tasks in a dashboard
- Mark tasks as complete
- Delete tasks
- Simple and clean user interface

---

## How It Works

Each task receives a priority score. Tasks with higher scores are shown first on the dashboard.

The priority score is currently calculated using:

```text
priority_score =
    urgency_score
  + workload_score
  + difficulty_score
  + importance_score
  - completion_score
```

The score is based on these factors:

- **Due date:** Tasks due sooner receive a higher urgency score.
- **Estimated hours:** Tasks that take longer receive a higher workload score.
- **Difficulty:** More difficult tasks receive a higher score.
- **Importance:** More important tasks receive a higher score.
- **Completion percentage:** Tasks that are closer to being finished receive a lower score.

This helps students focus on tasks that are urgent, important, time-consuming, and difficult.

---

## Tech Stack

This project is built with:

- Python
- Flask
- SQLite
- HTML
- CSS

---

## Project Structure

```text
study-prioritizer/
│
├── app.py
├── database.py
├── priority.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    └── add_task.html
```

---

## How to Run the Project Locally

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
```

2. Go into the project folder:

```bash
cd study-prioritizer
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

```bash
.\venv\Scripts\Activate
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

6. Run the Flask app:

```bash
python app.py
```

7. Open the website in your browser:

```text
http://127.0.0.1:5000
```

---

## Current Status

The current version of StudyPrioritizer allows users to:

- Add school tasks
- View tasks on a dashboard
- Automatically calculate priority scores
- Mark tasks as complete
- Delete tasks

The app currently runs locally using Flask and stores task data in a local SQLite database.

---

## Future Improvements

### Edit Tasks

A future version will allow users to edit tasks after creating them. This would let students update the task title, type, course, due date, estimated hours, difficulty, importance, and completion percentage without deleting and recreating the task.

### Priority Score Out of 10

The priority score will be changed to a simpler scale from 1 to 10. This would make the score easier to understand quickly.

### Color-Coded Priorities

Tasks will be color-coded based on their priority level. For example:

- Priority 9-10: red for very high priority
- Priority 7-8: orange for high priority
- Priority 5-6: yellow for medium priority
- Priority 3-4: green for low priority
- Priority 1-2: blue for very low priority

This would make the dashboard easier to read because users could quickly see which tasks need the most attention.

### Update Completion Percentage

Users will be able to update the completion percentage of a task directly from the dashboard. After the completion percentage changes, the priority score would automatically update.

### Filter and Sort Options

Users could filter or sort tasks by course, task type, due date, completion status, or priority level. This would make the app more useful when students have many tasks.

### Search Bar

A search bar could be added so users can quickly find a specific task, class, or assignment.

### Better Dashboard Design

The dashboard could be improved with task cards, icons, and a more responsive layout for smaller screens.

### Task Categories

Tasks could be grouped by course, task type, or priority level. This would make it easier to organize large amounts of schoolwork.

### Due Date Warnings

The app could show warnings for tasks that are overdue, due today, or due soon.

### Data Reset Option

A reset option could allow users to clear all tasks from the local database when starting a new semester or school term.

---

## Why I Made This Project

I made StudyPrioritizer to help students manage schoolwork in a more organized way. Instead of only looking at due dates, the app considers multiple factors that affect how urgent a task feels, such as difficulty, importance, estimated time, and completion progress.

This project also helped me practice building a full-stack web app using Flask, SQLite, HTML, and CSS.

---

## Author

Created by [Your Name].