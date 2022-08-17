import os
import json
import requests

base_url = os.environ.get("BASE_URL", "http://web:5000")

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiaWF0IjoxNjYwNzIzNzM2LCJleHAiOjE2NjA3MjQ5MzYsInN1YiI6NCwiZW1haWwiOiJ0ZXN0LmVyQGdtYWlsLmNvbSJ9.dWxwpYMDrrKlLHdfSNYpjf9JLNBQKzRHPAy0A47OCtY"

headers = {
    "Content-Type": "application/json",
}


def test_all_projects_details_url():
    response = requests.get(f"{base_url}/projects/details")
    response_body = response.json()

    assert (
        response.status_code == 200
        and response_body["message"] == "All Project Details"
    )


def test_projects_add_url():
    """Testing Adding a project"""

    data = {
        "project_name": "Test",
        "sampling_type": "Unified",
        "description": "Test is a project from a Rum M Er.",
        "instructions": "1st Learn 2nd Practise 3rd Work 4th Test",
    }
    endpoint = "/projects/add"

    # without tokens
    response = requests.post(
        f"{base_url}{endpoint}", headers=headers, data=json.dumps(data)
    )
    response_body = response.json()
    assert response.status_code == 401 and response_body["message"] == "Not authorized"

    # # with tokens
    # headers["Authorization"] = f"Bearer {access_token}"
    # response = requests.post(
    #     f"{base_url}{endpoint}", headers=headers, data=json.dumps(data)
    # )
    # response_body = response.json()
    # assert response.status_code == 201 and response_body["message"] == "New Project Test added"


def test_projects_edit_url():

    data = {
        "project_name": "Test",
        "sampling_type": "Unified",
        "description": "Test is a project from a Test Er.",
        "instructions": "1st Learn 2nd Practise 3rd Work 4th Test",
    }
    endpoint = "/projects/edit/10"

    # without tokens
    response = requests.put(
        f"{base_url}{endpoint}", headers=headers, data=json.dumps(data)
    )
    response_body = response.json()

    assert (
        response.status_code == 401
    )  # and response_body["message"] == "Not authorized"

    # # with tokens
    # headers["Authorization"] = f"Bearer {access_token}"
    # response = requests.put(
    #     f"{base_url}{endpoint}", headers=headers, data=json.dumps(data)
    # )
    # response_body = response.json()
    # assert response.status_code == 201 and response_body["message"] == "New Project Test added"


def test_projects_remove_url():
    endpoint = "/projects/remove/10"

    # without tokens
    response = requests.delete(f"{base_url}{endpoint}", headers=headers)
    response_body = response.json()

    assert response.status_code == 401 and response_body["message"] == "Not authorized"
