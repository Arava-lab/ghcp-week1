from fastapi.testclient import TestClient
from src import app as fastapi_app
import pytest

# Use fixtures from conftest.py

def test_get_activities(client):
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert isinstance(data["Chess Club"], dict)

def test_signup_success(client):
    response = client.post("/activities/Basketball%20Team/signup?email=tester@mergington.edu")
    assert response.status_code == 200
    assert "Signed up tester@mergington.edu for Basketball Team" in response.json()["message"]
    # Confirm participant added
    get_resp = client.get("/activities")
    assert "tester@mergington.edu" in get_resp.json()["Basketball Team"]["participants"]

def test_signup_activity_not_found(client):
    response = client.post("/activities/Nonexistent/signup?email=ghost@mergington.edu")
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"

def test_signup_already_signed_up(client):
    # Already in Chess Club: michael@mergington.edu
    response = client.post("/activities/Chess%20Club/signup?email=michael@mergington.edu")
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"

def test_unregister_success(client):
    # Remove daniel from Chess Club
    response = client.delete("/activities/Chess%20Club/signup?email=daniel@mergington.edu")
    assert response.status_code == 200
    assert "Removed daniel@mergington.edu from Chess Club" in response.json()["message"]
    # Confirm participant removed
    get_resp = client.get("/activities")
    assert "daniel@mergington.edu" not in get_resp.json()["Chess Club"]["participants"]

def test_unregister_activity_not_found(client):
    response = client.delete("/activities/Nonexistent/signup?email=ghost@mergington.edu")
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"

def test_unregister_participant_not_found(client):
    response = client.delete("/activities/Chess%20Club/signup?email=ghost@mergington.edu")
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"

def test_root_redirects_to_static(client):
    response = client.get("/")
    # Should redirect (307 or 302)
    assert response.status_code in (307, 302)
    assert "/static/index.html" in response.headers["location"]
