"""Класс Project и функции работы с проектами."""

from typing import List


class Project:
    """Проект, в котором ведётся учёт технического долга."""

    def __init__(self, project_id: int, name: str, description: str) -> None:
        """Создать проект."""
        self.id = project_id
        self.name = name
        self.description = description

    def __str__(self) -> str:
        """Строковое представление проекта."""
        return f"[{self.id}] {self.name} — {self.description}"

    @classmethod
    def from_data(cls, data: dict) -> "Project":
        """Создать Project из словаря."""
        return cls(
            project_id=data["id"],
            name=data["name"],
            description=data["description"],
        )

    def to_data(self) -> dict:
        """Преобразовать в словарь."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }


def add_project(projects: List[Project], name: str, description: str) -> Project:
    """Создать проект, добавить в коллекцию, вернуть объект."""
    new_id = max((p.id for p in projects), default=0) + 1
    project = Project(new_id, name, description)
    projects.append(project)
    return project


def find_project(projects: List[Project], query: str) -> List[Project]:
    """Найти проекты по подстроке названия."""
    q = query.lower()
    return [p for p in projects if q in p.name.lower()]


def find_project_by_id(projects: List[Project], project_id: int) -> Project | None:
    """Найти проект по id."""
    for p in projects:
        if p.id == project_id:
            return p
    return None


def show_projects(projects: List[Project]) -> None:
    """Вывести список проектов."""
    if not projects:
        print("Проектов нет.")
        return
    for p in projects:
        print(p)