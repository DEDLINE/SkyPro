import requests
import pytest
from lesson_08.yougile_api import YougileAPI
from datetime import datetime


@pytest.fixture(scope="session")
def api_client():
    return YougileAPI()


@pytest.fixture
def setup_project(api_client):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    initial_title = f"Test Project {timestamp}"

    response = api_client.create_project(title=initial_title)
    assert response.status_code == 200, ("Ошибка при создании "
                                         "проекта в Setup.")
    project_id = response.json().get("id")

    yield project_id

    if project_id:
        api_client.delete_project(project_id)


def test_create_project_positive(api_client):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_title = f"New Project {timestamp}"

    response = api_client.create_project(title=test_title)

    assert response.status_code == 200
    assert response.json().get("title") == test_title
    assert "id" in response.json()

    project_id = response.json().get("id")
    api_client.delete_project(project_id)


def test_create_project_negative_missing_title(api_client):
    url = f"{api_client.BASE_URL}/projects"

    response = requests.post(url, headers=api_client.headers, json={})

    assert response.status_code == 400
    assert "error" in response.json()


def test_get_project_positive(api_client, setup_project):
    project_id = setup_project

    response = api_client.get_project(project_id)

    assert response.status_code == 200
    assert response.json().get("id") == project_id
    assert "title" in response.json()


def test_get_project_negative_invalid_id(api_client):
    invalid_id = "00000000-0000-0000-0000-000000000000"

    response = api_client.get_project(invalid_id)

    assert response.status_code == 404
    assert "error" in response.json()


def test_update_project_positive(api_client, setup_project):
    project_id = setup_project
    new_title = "Updated Project Title " + datetime.now().strftime("%H%M")

    response = api_client.update_project(project_id, new_title)

    assert response.status_code == 200
    assert response.json().get("id") == project_id
    assert response.json().get("title") == new_title


def test_update_project_negative_invalid_id(api_client):
    invalid_id = "00000000-0000-0000-0000-000000000000"
    test_title = "Update Attempt"

    response = api_client.update_project(invalid_id, test_title)

    assert response.status_code == 404
    assert "error" in response.json()
