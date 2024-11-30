import pytest

from blog.factories import PostFactory

@pytest.fixture
def post_published():
    return PostFactory(title='pytest with fcatory')

@pytest.mark.django_db
def test_create_published(post_published):
    assert post_published.title == 'pytest with fcatory'