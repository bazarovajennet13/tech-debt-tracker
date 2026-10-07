from debts import (add_debt, find_debt, filter_by_project,
                   close_debt, delete_debt, statistics)


def test_add_debt():
    debts = []
    add_debt(debts, "Test", 1, 1, 1)
    assert len(debts) == 1
    assert debts[0]["closed"] is False


def test_find_debt():
    debts = []
    add_debt(debts, "Устаревшая библиотека", 1, 1, 1)
    assert find_debt(debts, "библиотека")
    assert not find_debt(debts, "тесты")


def test_filter_by_project():
    debts = []
    add_debt(debts, "A", 1, 1, 1)
    add_debt(debts, "B", 2, 1, 1)
    assert len(filter_by_project(debts, 1)) == 1


def test_close_and_statistics():
    debts = []
    add_debt(debts, "A", 1, 1, 1)
    add_debt(debts, "B", 1, 1, 1)
    close_debt(debts, 1)
    assert statistics(debts) == {"total": 2, "closed": 1, "open": 1}


def test_delete_debt():
    debts = []
    add_debt(debts, "A", 1, 1, 1)
    assert delete_debt(debts, 1)
    assert len(debts) == 0