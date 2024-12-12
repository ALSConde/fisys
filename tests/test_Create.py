from fastapi.testclient import TestClient
from fastapi import status
import pytest
from main import app
from unittest.mock import AsyncMock

client = TestClient(app)


@pytest.fixture
def mock_create_service(monkeypatch):
    mock_service = AsyncMock()
    monkeypatch.setattr("routes.v1.userRoutes.Create.CreateService", mock_service)
    return mock_service


def test_create_user_success(mock_create_service):
    mock_create_service.execute.return_value = {"id": 1, "name": "John Doe"}
    response = client.post(
        "v1/user/create/",
        json={"name": "John Doe", "email": "john@example.com", "password": "password"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"detail": "User created successfully"}

    # Rollback on database
    mock_create_service.rollback.assert_called_once()


def test_create_user_conflict(mock_create_service):
    mock_create_service.execute.return_value = Exception("User already exists")
    response = client.post(
        "v1/user/create/",
        json={"name": "John Doe", "email": "john@example.com", "password": "password"},
    )
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json() == {"detail": "User already exists"}


def test_create_user_bad_request():
    response = client.post("v1/user/create/", json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    mock_create_service.execute.assert_called_once()


def test_create_user_internal_server_error(mock_create_service):
    mock_create_service.execute.side_effect = Exception("Unexpected error")
    response = client.post(
        "v1/user/create/",
        json={"name": "John Doe", "email": "john@example.com", "password": "password"},
    )
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.json() == {"detail": "Internal server error"}

    mock_create_service.execute.assert_called_once()
