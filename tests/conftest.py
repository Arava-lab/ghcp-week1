import pytest
from src import app as fastapi_app
from fastapi.testclient import TestClient

# Original activities state for reset
def get_initial_activities():
    return {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Competitive basketball practices and games",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 15,
            "participants": []
        },
        "Swimming Club": {
            "description": "Swim training and water polo",
            "schedule": "Wednesdays, 5:00 PM - 7:00 PM",
            "max_participants": 20,
            "participants": []
        },
        "Painting Workshop": {
            "description": "Explore different painting techniques and create art",
            "schedule": "Mondays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": []
        },
        "Drama Club": {
            "description": "Acting rehearsals and stage performances",
            "schedule": "Fridays, 4:00 PM - 6:00 PM",
            "max_participants": 20,
            "participants": []
        },
        "Science Olympiad": {
            "description": "Prepare for academic competitions in science and engineering",
            "schedule": "Thursdays, 3:30 PM - 5:30 PM",
            "max_participants": 25,
            "participants": []
        },
        "Debate Society": {
            "description": "Practice debate skills and participate in tournaments",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 30,
            "participants": []
        }
    }

@pytest.fixture(autouse=True)
def reset_activities(monkeypatch):
    # Patch the activities dict in src.app
    from src import app as app_module
    app_module.activities.clear()
    app_module.activities.update(get_initial_activities())
    yield

@pytest.fixture
def client():
    return TestClient(fastapi_app.app)
