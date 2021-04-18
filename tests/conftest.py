import pytest

from app import app as flask_app


@pytest.fixture
def client():
    with flask_app.test_client() as test_client:
        with flask_app.app_context():
            yield test_client
