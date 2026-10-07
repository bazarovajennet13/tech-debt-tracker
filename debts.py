"""Работа с задачами технического долга."""


def add_debt(debts: list, title: str, project_id: int,
             author_id: int, priority_id: int) -> dict:
    """Добавить задачу долга."""
    debt = {
        "id": max((d["id"] for d in debts), default=0) + 1,
        "title": title,
        "project_id": project_id,
        "author_id": author_id,
        "priority_id": priority_id,
        "closed": False,
    }
    debts.append(debt)
    return debt


def find_debt(debts: list, query: str) -> list:
    """Найти задачи по подстроке в названии."""
    q = query.lower()
    return [d for d in debts if q in d["title"].lower()]


def filter_by_project(debts: list, project_id: int) -> list:
    """Задачи конкретного проекта."""
    return [d for d in debts if d["project_id"] == project_id]


def filter_by_author(debts: list, author_id: int) -> list:
    """Задачи конкретного автора."""
    return [d for d in debts if d["author_id"] == author_id]


def filter_by_priority(debts: list, priority_id: int) -> list:
    """Задачи конкретного приоритета."""
    return [d for d in debts if d["priority_id"] == priority_id]


def sort_by_priority(debts: list, priorities: dict) -> list:
    """Сортировка по весу приоритета (по убыванию) через lambda."""
    return sorted(
        debts,
        key=lambda d: priorities.get(d["priority_id"], {}).get("weight", 0),
        reverse=True,
    )


def close_debt(debts: list, debt_id: int) -> bool:
    """Закрыть задачу."""
    for d in debts:
        if d["id"] == debt_id:
            d["closed"] = True
            return True
    return False


def delete_debt(debts: list, debt_id: int) -> bool:
    """Удалить задачу."""
    for d in debts:
        if d["id"] == debt_id:
            debts.remove(d)
            return True
    return False


def statistics(debts: list) -> dict:
    """Статистика: всего / закрыто / открыто."""
    total = len(debts)
    closed = sum(1 for d in debts if d["closed"])
    return {"total": total, "closed": closed, "open": total - closed}