"""Класс Author и функции работы с авторами."""

from typing import List


class Author:
    """Автор задачи технического долга."""

    def __init__(self, author_id: int, name: str, email: str) -> None:
        """Создать автора."""
        self.id = author_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        """Строковое представление автора."""
        return f"[{self.id}] {self.name} — {self.email}"

    @classmethod
    def from_data(cls, data: dict) -> "Author":
        """Создать Author из словаря (например, из JSON)."""
        return cls(
            author_id=data["id"],
            name=data["name"],
            email=data["email"],
        )

    def to_data(self) -> dict:
        """Преобразовать в словарь для сохранения в JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }


def add_author(authors: List[Author], name: str, email: str) -> Author:
    """Создать автора, добавить в коллекцию, вернуть объект."""
    new_id = max((a.id for a in authors), default=0) + 1
    author = Author(new_id, name, email)
    authors.append(author)
    return author


def find_author(authors: List[Author], query: str) -> List[Author]:
    """Найти авторов по подстроке имени (без учёта регистра)."""
    q = query.lower()
    return [a for a in authors if q in a.name.lower()]


def find_author_by_id(authors: List[Author], author_id: int) -> Author | None:
    """Найти автора по id. Если нет — вернуть None."""
    for a in authors:
        if a.id == author_id:
            return a
    return None


def show_authors(authors: List[Author]) -> None:
    """Вывести список авторов."""
    if not authors:
        print("Авторов нет.")
        return
    for a in authors:
        print(a)