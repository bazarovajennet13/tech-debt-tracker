"""Класс Debt и функции работы с задачами технического долга."""

from typing import List, Optional
from .projects import Project
from .authors import Author
from .priorities import Priority


class Debt:
    """Задача технического долга."""

    def __init__(
        self,
        debt_id: int,
        title: str,
        project: Project,
        author: Author,
        priority: Priority,
        is_closed: bool = False,
    ) -> None:
        """Создать задачу долга со ссылками на Project, Author, Priority."""
        self.id = debt_id
        self.title = title
        self.project = project
        self.author = author
        self.priority = priority
        self.is_closed = is_closed

    def close(self) -> None:
        """Закрыть задачу."""
        self.is_closed = True

    def __str__(self) -> str:
        """Строковое представление задачи."""
        mark = "✔" if self.is_closed else "✗"
        return (
            f"[{self.id}] {mark} {self.title} | "
            f"{self.project.name} | {self.author.name} | {self.priority.name}"
        )

    @classmethod
    def from_data(
        cls,
        data: dict,
        projects: List[Project],
        authors: List[Author],
        priorities: List[Priority],
    ) -> Optional["Debt"]:
        """Создать Debt из словаря, найдя Project, Author и Priority по id."""
        project = next((p for p in projects if p.id == data["project_id"]), None)
        author = next((a for a in authors if a.id == data["author_id"]), None)
        priority = next((p for p in priorities if p.id == data["priority_id"]), None)
        if project is None or author is None or priority is None:
            return None
        return cls(
            debt_id=data["id"],
            title=data["title"],
            project=project,
            author=author,
            priority=priority,
            is_closed=data.get("is_closed", False),
        )

    def to_data(self) -> dict:
        """Преобразовать в словарь для JSON (храним только id связанных объектов)."""
        return {
            "id": self.id,
            "title": self.title,
            "project_id": self.project.id,
            "author_id": self.author.id,
            "priority_id": self.priority.id,
            "is_closed": self.is_closed,
        }


def add_debt(
    debts: List[Debt],
    title: str,
    project: Project,
    author: Author,
    priority: Priority,
) -> Debt:
    """Создать задачу долга, добавить в коллекцию, вернуть объект."""
    new_id = max((d.id for d in debts), default=0) + 1
    debt = Debt(new_id, title, project, author, priority)
    debts.append(debt)
    return debt


def find_debt(debts: List[Debt], query: str) -> List[Debt]:
    """Найти задачи по подстроке в названии."""
    q = query.lower()
    return [d for d in debts if q in d.title.lower()]


def filter_by_project(debts: List[Debt], project: Project) -> List[Debt]:
    """Задачи конкретного проекта."""
    return [d for d in debts if d.project.id == project.id]


def filter_by_author(debts: List[Debt], author: Author) -> List[Debt]:
    """Задачи конкретного автора."""
    return [d for d in debts if d.author.id == author.id]


def filter_by_priority(debts: List[Debt], priority: Priority) -> List[Debt]:
    """Задачи конкретного приоритета."""
    return [d for d in debts if d.priority.id == priority.id]


def sort_by_priority(debts: List[Debt]) -> List[Debt]:
    """Сортировка по весу приоритета (по убыванию)."""
    return sorted(debts, key=lambda d: d.priority.weight, reverse=True)


def close_debt(debts: List[Debt], debt_id: int) -> bool:
    """Найти задачу и закрыть её через метод close()."""
    for d in debts:
        if d.id == debt_id:
            d.close()
            return True
    return False


def delete_debt(debts: List[Debt], debt_id: int) -> bool:
    """Удалить задачу по id."""
    for d in debts:
        if d.id == debt_id:
            debts.remove(d)
            return True
    return False


def statistics(debts: List[Debt]) -> dict:
    """Статистика: всего / закрыто / открыто."""
    total = len(debts)
    closed = sum(1 for d in debts if d.is_closed)
    return {"total": total, "closed": closed, "open": total - closed}


def show_debts(debts: List[Debt]) -> None:
    """Вывести список задач."""
    if not debts:
        print("Задач долга нет.")
        return
    for d in debts:
        print(d)