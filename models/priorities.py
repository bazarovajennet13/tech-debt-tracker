"""Класс Priority и функции работы с приоритетами."""

from typing import List


class Priority:
    """Приоритет задачи долга с весом от 1 до 5."""

    def __init__(self, priority_id: int, name: str, weight: int) -> None:
        """Создать приоритет."""
        if not 1 <= weight <= 5:
            raise ValueError("Вес приоритета должен быть от 1 до 5")
        self.id = priority_id
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        """Строковое представление приоритета."""
        return f"[{self.id}] {self.name} (вес {self.weight})"

    @classmethod
    def from_data(cls, data: dict) -> "Priority":
        """Создать Priority из словаря."""
        return cls(
            priority_id=data["id"],
            name=data["name"],
            weight=data["weight"],
        )

    def to_data(self) -> dict:
        """Преобразовать в словарь."""
        return {
            "id": self.id,
            "name": self.name,
            "weight": self.weight,
        }


def add_priority(priorities: List[Priority], name: str, weight: int) -> Priority:
    """Создать приоритет, добавить в коллекцию, вернуть объект."""
    new_id = max((p.id for p in priorities), default=0) + 1
    priority = Priority(new_id, name, weight)
    priorities.append(priority)
    return priority


def find_priority_by_id(priorities: List[Priority], priority_id: int) -> Priority | None:
    """Найти приоритет по id."""
    for p in priorities:
        if p.id == priority_id:
            return p
    return None


def show_priorities(priorities: List[Priority]) -> None:
    """Вывести список приоритетов."""
    if not priorities:
        print("Приоритетов нет.")
        return
    for p in priorities:
        print(p)