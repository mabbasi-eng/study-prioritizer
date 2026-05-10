from datetime import datetime

def calculate_priority(due_date, estimated_hrs, difficulty, importance, completion):
    urgency_score = calculate_urgency_score(due_date)
    workload_score = calculate_workload_score(estimated_hrs)
    difficulty_score = calculate_difficulty_score(difficulty)
    importance_score = calculate_importance_score(importance)
    completion_score = calculate_completion_score(completion)

    priority_score = (
        urgency_score
        + workload_score
        + difficulty_score
        + importance_score
        - completion_score
    )

    # This prevents the priority score from going below 0.
    # Example: a completed task should not have a negative score.
    if priority_score < 0:
        priority_score = 0

    # Round the score so it looks cleaner on the website.
    return round(priority_score, 2)

#calculate urgency based on deadline; Shorter deadlines = higher score
def calculate_urgency_score(due_date):
    # Convert the due_date string into an actual date object.
    # HTML date inputs usually give dates in this format: YYYY-MM-DD
    due = datetime.strptime(due_date, "%Y-%m-%d").date()

    # Get today's date.
    today = datetime.today().date()

    # Find how many days are left until the task is due.
    days_left = (due - today).days

    # If the task is overdue, make it very urgent.
    if days_left < 0:
        return 50

    # If it is due today, make it very urgent.
    elif days_left == 0:
        return 45

    # Due tomorrow.
    elif days_left == 1:
        return 40

    # Due within 3 days.
    elif days_left <= 3:
        return 30

    # Due within a week.
    elif days_left <= 7:
        return 20

    # Due within two weeks.
    elif days_left <= 14:
        return 10

    # Due later than two weeks from now.
    else:
        return 5

#Calculate workload based on how long the task will take. 
def calculate_workload_score(estimated_hrs):
    # Each estimated hour adds 2 points.
    # Example: 3 hours = 6 points.
    return estimated_hrs * 2

#Calculate based on difficulty (1-5)
def calculate_difficulty_score(difficulty):
    # Each difficulty level adds 3 points.
    # Example: difficulty 4 = 12 points.
    return difficulty * 3

#Caluculate based on importance (1-5)
def calculate_importance_score(importance):
    # Each importance level adds 4 points.
    # Example: importance 5 = 20 points.
    return importance * 4


def calculate_completion_score(completion):
    # Divide by 5 so completion lowers the score gradually.
    # Example: 50% complete removes 10 points.
    # Example: 100% complete removes 20 points.
    return completion / 5