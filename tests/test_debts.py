from models import Author, Project, Priority, Debt
from models.debts import (add_debt, find_debt, filter_by_project,
                          close_debt, delete_debt, statistics)


def make_objects():
    project = Project(1, "API", "Backend")
    author = Author(1, "Иван", "ivan@example.com")
    priority = Priority(1, "Высокий", 5)
    return project, author, priority


def test_debt_creation():
    project, author, priority = make_objects()
    debt = Debt(1, "Нет тестов", project, author, priority)
    assert debt.id == 1
    assert debt.project is project
    assert debt.author is author
    assert debt.priority is priority
    assert debt.is_closed is False


def test_debt_close():
    project, author, priority = make_objects()
    debt = Debt(1, "Нет тестов", project, author, priority)
    debt.close()
    assert debt.is_closed is True


def test_add_debt():
    project, author, priority = make_objects()
    debts = []
    add_debt(debts, "Тест", project, author, priority)
    assert len(debts) == 1


def test_find_debt():
    project, author, priority = make_objects()
    debts = []
    add_debt(debts, "Устаревшая библиотека", project, author, priority)
    assert find_debt(debts, "библиотека")
    assert not find_debt(debts, "тесты")


def test_filter_by_project():
    project1, author, priority = make_objects()
    project2 = Project(2, "Mobile", "App")
    debts = []
    add_debt(debts, "A", project1, author, priority)
    add_debt(debts, "B", project2, author, priority)
    assert len(filter_by_project(debts, project1)) == 1


def test_close_and_statistics():
    project, author, priority = make_objects()
    debts = []
    add_debt(debts, "A", project, author, priority)
    add_debt(debts, "B", project, author, priority)
    close_debt(debts, 1)
    assert statistics(debts) == {"total": 2, "closed": 1, "open": 1}


def test_delete_debt():
    project, author, priority = make_objects()
    debts = []
    add_debt(debts, "A", project, author, priority)
    assert delete_debt(debts, 1)
    assert len(debts) == 0