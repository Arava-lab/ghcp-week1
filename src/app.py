"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
activities = [
    {
        "id": 1,
        "name": "Basketball",
        "type": "sport",
        "participants": [],
    },
    {
        "id": 2,
        "name": "Soccer",
        "type": "sport",
        "participants": [],
    },
    # Added sports activities
    {
        "id": 3,
        "name": "Tennis",
        "type": "sport",
        "participants": [],
    },
    {
        "id": 4,
        "name": "Swimming",
        "type": "sport",
        "participants": [],
    },
    {
        "id": 5,
        "name": "Painting",
        "type": "artistic",
        "participants": [],
    },
    {
        "id": 6,
        "name": "Drama Club",
        "type": "artistic",
        "participants": [],
    },
    # Added artistic activities
    {
        "id": 7,
        "name": "Photography",
        "type": "artistic",
        "participants": [],
    },
    {
        "id": 8,
        "name": "Choir",
        "type": "artistic",
        "participants": [],
    },
    {
        "id": 9,
        "name": "Chess Club",
        "type": "intellectual",
        "participants": [],
    },
    {
        "id": 10,
        "name": "Mathletes",
        "type": "intellectual",
        "participants": [],
    },
    # Added intellectual activities
    {
        "id": 11,
        "name": "Debate Team",
        "type": "intellectual",
        "participants": [],
    },
    {
        "id": 12,
        "name": "Science Olympiad",
        "type": "intellectual",
        "participants": [],
    },
]

@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    # Validate student is not already signed up
    if email in activities[activity_name]["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up")
    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
