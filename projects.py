"""Работа с проектами."""


def add_project(projects: dict, name: str, description: str) -> int:
    """Добавить проект. Возвращает id."""
    new_id = max(projects.keys(), default=0) + 1
    projects[new_id] = {"name": name, "description": description}
    return new_id


def find_project(projects: dict, query: str) -> list:
    """Найти проекты по подстроке названия."""
    q = query.lower()
    return [(pid, p) for pid, p in projects.items() if q in p["name"].lower()]


def get_project_name(projects: dict, project_id: int) -> str:
    """Название проекта по id (или '?' если нет)."""
    return projects.get(project_id, {}).get("name", "?")