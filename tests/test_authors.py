from models import Author
from models.authors import add_author, find_author, find_author_by_id


def test_author_creation():
    author = Author(1, "Иван", "ivan@example.com")
    assert author.id == 1
    assert author.name == "Иван"
    assert author.email == "ivan@example.com"


def test_author_str():
    author = Author(1, "Иван", "ivan@example.com")
    assert "Иван" in str(author)


def test_add_author():
    authors = []
    author = add_author(authors, "Иван", "ivan@example.com")
    assert len(authors) == 1
    assert author.name == "Иван"


def test_find_author():
    authors = []
    add_author(authors, "Иван Иванов", "ivan@example.com")
    assert find_author(authors, "иван")
    assert not find_author(authors, "пётр")


def test_find_author_by_id():
    authors = []
    add_author(authors, "Иван", "ivan@example.com")
    assert find_author_by_id(authors, 1) is not None
    assert find_author_by_id(authors, 99) is None