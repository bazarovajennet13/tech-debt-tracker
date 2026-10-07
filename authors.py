"""Работа с авторами задач технического долга."""


def add_author(authors: dict, name: str, email: str) -> int:
    """Добавить автора. Возвращает id нового автора."""
    new_id = max(authors.keys(), default=0) + 1
    authors[new_id] = {"name": name, "email": email}
    return new_id


def find_author(authors: dict, query: str) -> list:
    """Найти авторов по подстроке имени (без учёта регистра)."""
    q = query.lower()
    return [(aid, a) for aid, a in authors.items() if q in a["name"].lower()]


def get_author_name(authors: dict, author_id: int) -> str:
    """Имя автора по id (или '?' если не найден)."""
    return authors.get(author_id, {}).get("name", "?")