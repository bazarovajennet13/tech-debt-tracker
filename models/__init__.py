"""Модели предметной области: Автор, Проект, Приоритет, Задача долга."""

from .authors import Author
from .projects import Project
from .priorities import Priority
from .debts import Debt

__all__ = ["Author", "Project", "Priority", "Debt"]