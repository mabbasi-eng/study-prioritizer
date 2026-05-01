# StudyPrioritizer

StudyPrioritizer is a web app designed to help students decide what school task they should work on first. Students can enter assignments, tests, labs, quizzes, projects, and other academic tasks, and the app calculates a priority score based on due date, estimated time needed, difficulty, course importance, and completion status.

The goal of this project is to create a simple but useful productivity tool for students who want a clearer way to manage academic workload.

---

## Features

- Add academic tasks
- Store tasks in a local database
- Rank tasks automatically by priority
- Calculate priority using multiple factors:
  - Due date
  - Estimated hours needed
  - Task difficulty
  - Course importance
  - Completion percentage
- View all tasks in a dashboard
- Mark tasks as complete
- Delete tasks
- Simple and clean user interface

---

## Tech Stack

This project is built using:

- Python
- Flask
- SQLite
- HTML
- CSS

---

## How It Works

Each task receives a priority score. Tasks with higher scores are shown first on the dashboard.

The priority score is calculated using:

```text
priority_score =
    urgency_score
  + workload_score
  + difficulty_score
  + importance_score
  - completion_score
