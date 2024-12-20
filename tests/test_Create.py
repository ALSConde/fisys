from pydantic import SecretStr
import pytest
from fastapi.testclient import TestClient
from fastapi import status
from unittest.mock import patch
from schemas.pydantic.user import UserPost
from exceptions.user.UserAlreadyExists import UserAlreadyExists
from main import app

client = TestClient(app, base_url="http://localhost:8000/v1")


@pytest.fixture
def user_data():
    return {
        "name": "testuser",
        "email": "testuser@example.com",
        "password": "password123",
    }


def test_create_user_success(user_data):
    with patch("services.user.CreateService.CreateService.execute") as mock_execute:
        mock_execute.return_value = None
        response = client.post(
            "/user/create/",
            json={
                "name": "testuser",
                "email": "testuser@example.com",
                "password": "password123",
            },
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.content == b'{"detail":"User created successfully"}'


def test_create_user_already_exists(user_data):
    with patch("services.user.CreateService.CreateService.execute") as mock_execute:
        mock_execute.side_effect = UserAlreadyExists("User already exists")
        response = client.post("/user/create/", json=user_data)
        assert response.status_code == status.HTTP_409_CONFLICT
        assert response.json() == {"detail": "User already exists"}


def test_create_user_invalid_data():
    invalid_data = {
        "username": "testuser",
        "email": "invalid-email",
        "password": "short",
    }
    response = client.post("/user/create/", json=invalid_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
