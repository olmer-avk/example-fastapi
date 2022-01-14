import pytest

from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get('/posts')
    post_map = map(lambda p: schemas.PostResponse(**p), res.json())
    posts_list = list(post_map)

    assert res.status_code == 200
    assert len(res.json()) == len(test_posts)
    # assert posts_list[0].Post.id == test_posts[0].id


def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get('/posts')
    assert res.status_code == 401


def test_unauthorized_user_get_ont_post(client, test_posts):
    res = client.get(f'/posts/{test_posts[0].id}')
    assert res.status_code == 401


def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get('/posts/88888888')
    assert res.status_code == 404


def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f'/posts/{test_posts[0].id}')
    assert res.status_code == 200
    post = schemas.PostResponse(**res.json())

    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert post.Post.title == test_posts[0].title


@pytest.mark.parametrize("title, content, published", [
    ("awesome new title", "awesome new content", True),
    ("favorite pizza", "i love pepperoni", False),
    ("tallest skyscrapers", "wahoo", True)
])
def test_create_post(authorized_client, test_user, title, content, published):
    res = authorized_client.post(f'/posts', json={"title": title, "content": content, "published": published})
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published



