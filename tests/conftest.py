import pytest


@pytest.fixture
def app():
    from app import create_app
    
    return create_app()


@pytest.fixture
def client(app):
    return app.test_client()
