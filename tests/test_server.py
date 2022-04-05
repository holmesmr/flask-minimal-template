import pytest


def test_hello(client):
    """Ensure that the Hello endpoint returns a successful status code."""

    response = client.get("/")
    assert response.status_code == 200
    assert response.is_json
    assert response.json["content"] == "Hello, world!"
