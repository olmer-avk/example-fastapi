from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pytest
from alembic import command
from alembic.config import Config

from app.main import app
from app.config import settings
from app.database import get_db, Base
from app.oauth2 import create_acccess_token
from app import models


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'
# alembic_cfg = Config("./alembic.ini")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base = declarative_base()

# client = TestClient(app)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # command.upgrade(alembic_cfg, 'head')
    # yield TestClient(app)
    # #command.downgrade(alembic_cfg, 'base')
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user(client):
    user_data = {'email': 'hello1@mail.ru', 'password': '123'}
    res = client.post('/users', json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def test_user2(client):
    user_data = {'email': 'hello123@mail.ru', 'password': '123'}
    res = client.post('/users', json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def token(test_user):
    return create_acccess_token(data={"user_id": test_user['id']})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {**client.headers, "Authorization": f"Bearer {token}"}

    return client


@pytest.fixture
def test_posts(test_user, test_user2, session):
    posts_data = [
        {"title": "first title", "content": "first content", "owner_id": test_user['id']},
        {"title": "second title", "content": "second content", "owner_id": test_user['id']},
        {"title": "third title", "content": "third content", "owner_id": test_user['id']},
        {"title": "sdfdsf title", "content": "dfdf content", "owner_id": test_user2['id']}
    ]

    post_map = map(lambda d: models.Post(**d), posts_data)
    post_map = list(post_map)
    session.add_all(post_map)

    session.commit()
    posts = session.query(models.Post).all()
    return posts


