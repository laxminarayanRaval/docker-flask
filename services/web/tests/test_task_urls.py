import json
import requests

from . import base_url, auth_headers


def test_project_id_vise_task():
    endpoint = "/task/project/13"
    response = requests.get(f"{base_url}{endpoint}", headers=auth_headers)

    assert response.status_code == 200

    response_body = response.json()
    assert isinstance(response_body["data"], list)


def test_add_task():
    data = {"project_id": "13", "title": "", "comment": ""}

    endpoint = "/task/add"
    response = requests.post(
        f"{base_url}{endpoint}", headers=auth_headers, data=json.dumps(data)
    )

    assert response.status_code == 201

    response_body = response.json()

    assert isinstance(response_body["message"], str)


def test_update_task_status():
    data = {"status": "submitted"}
    endpoint = "/task/status/40"

    response = requests.put(
        f"{base_url}{endpoint}", headers=auth_headers, data=json.dumps(data)
    )

    assert response.status_code == 200

    response_body = response.json()
    assert response_body["message"] == "Task:40 has been updated"
