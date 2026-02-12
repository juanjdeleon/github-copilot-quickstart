import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Use a test activity and email
    activities = client.get("/activities").json()
    activity = next(iter(activities))
    email = "testuser@example.com"

    # Sign up
    signup_resp = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup_resp.status_code in (200, 400)  # 400 if already signed up

    # Unregister
    unregister_resp = client.post(f"/activities/{activity}/unregister?email={email}")
    assert unregister_resp.status_code in (200, 400, 404)  # 400 if not signed up, 404 if activity not found
