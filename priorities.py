"""Работа с приоритетами задач долга."""


def add_priority(priorities: dict, name: str, weight: int) -> int:
    """Добавить приоритет. weight — число от 1 до 5."""
    if not 1 <= weight <= 5:
        raise ValueError("Вес приоритета должен быть от 1 до 5")
    new_id = max(priorities.keys(), default=0) + 1
    priorities[new_id] = {"name": name, "weight": weight}
    return new_id


def get_priority_name(priorities: dict, priority_id: int) -> str:
    """Название приоритета по id (или '?' если нет)."""
    return priorities.get(priority_id, {}).get("name", "?")


def get_priority_weight(priorities: dict, priority_id: int) -> int:
    """Вес приоритета по id (или 0 если нет)."""
    return priorities.get(priority_id, {}).get("weight", 0)