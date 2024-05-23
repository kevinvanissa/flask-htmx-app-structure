import pytest
from config import Config
from werkzeug.security import generate_password_hash
from app import create_app, db
from app.models import User

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED = False


@pytest.fixture()
def app():
    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()
        user1 = User(username='kevin', email='kevin@gmail.com', password=generate_password_hash('1234'))
        db.session.add(user1)
        db.session.commit()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()

