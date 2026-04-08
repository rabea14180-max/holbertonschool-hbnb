import pytest
from app import create_app, db
from app.api import create_api
from config import DevelopmentConfig


@pytest.fixture
def app():
    """Flask app with in-memory SQLite so tests do not touch development.db."""
    application = create_app(DevelopmentConfig)
    application.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
    )
    create_api(application)
    with application.app_context():
        db.create_all()
    yield application
    with application.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
