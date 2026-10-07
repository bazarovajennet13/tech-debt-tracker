"""Сохранение и загрузка данных в JSON с преобразованием в объекты."""

import json
import os
from typing import List
from models import Author, Project, Priority, Debt


def _load_json(filename: str, default):
    if not os.path.exists(filename):
        return default
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Ошибка чтения {filename}. Использую значение по умолчанию.")
        return default


def _save_json(filename: str, data) -> None:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_authors(filename: str) -> List[Author]:
    """Загрузить авторов из JSON и преобразовать в объекты Author."""
    data = _load_json(filename, [])
    return [Author.from_data(item) for item in data]


def save_authors(filename: str, authors: List[Author]) -> None:
    """Сохранить авторов в JSON."""
    _save_json(filename, [a.to_data() for a in authors])


def load_projects(filename: str) -> List[Project]:
    """Загрузить проекты из JSON."""
    data = _load_json(filename, [])
    return [Project.from_data(item) for item in data]


def save_projects(filename: str, projects: List[Project]) -> None:
    """Сохранить проекты в JSON."""
    _save_json(filename, [p.to_data() for p in projects])


def load_priorities(filename: str) -> List[Priority]:
    """Загрузить приоритеты из JSON."""
    data = _load_json(filename, [])
    return [Priority.from_data(item) for item in data]


def save_priorities(filename: str, priorities: List[Priority]) -> None:
    """Сохранить приоритеты в JSON."""
    _save_json(filename, [p.to_data() for p in priorities])


def load_debts(
    filename: str,
    projects: List[Project],
    authors: List[Author],
    priorities: List[Priority],
) -> List[Debt]:
    """Загрузить задачи долга, восстановив связи с проектами, авторами, приоритетами."""
    data = _load_json(filename, [])
    result: List[Debt] = []
    for item in data:
        debt = Debt.from_data(item, projects, authors, priorities)
        if debt is not None:
            result.append(debt)
    return result


def save_debts(filename: str, debts: List[Debt]) -> None:
    """Сохранить задачи долга в JSON (только id связанных объектов)."""
    _save_json(filename, [d.to_data() for d in debts])