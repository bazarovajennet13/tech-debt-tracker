"""Система учёта технического долга — точка входа."""

from storage import load_dict, load_list, save_json
from models.authors import add_author, find_author, get_author_name
from models.projects import add_project, find_project, get_project_name
from models.priorities import add_priority, get_priority_name, get_priority_weight
from models.debts import (add_debt, find_debt, filter_by_project, filter_by_author,
                   filter_by_priority, sort_by_priority, close_debt,
                   delete_debt, statistics)
from utils import input_int

AUTHORS_FILE = "data/authors.json"
PROJECTS_FILE = "data/projects.json"
PRIORITIES_FILE = "data/priorities.json"
DEBTS_FILE = "data/debts.json"


def show_authors(authors: dict) -> None:
    if not authors:
        print("Авторов нет.")
        return
    for aid, a in authors.items():
        print(f"[{aid}] {a['name']} — {a['email']}")


def show_projects(projects: dict) -> None:
    if not projects:
        print("Проектов нет.")
        return
    for pid, p in projects.items():
        print(f"[{pid}] {p['name']} — {p['description']}")


def show_priorities(priorities: dict) -> None:
    if not priorities:
        print("Приоритетов нет.")
        return
    for pid, p in priorities.items():
        print(f"[{pid}] {p['name']} (вес {p['weight']})")


def show_debts(debts: list, projects: dict, authors: dict, priorities: dict) -> None:
    if not debts:
        print("Задач долга нет.")
        return
    for d in debts:
        mark = "✔" if d["closed"] else "✗"
        pname = get_project_name(projects, d["project_id"])
        aname = get_author_name(authors, d["author_id"])
        prname = get_priority_name(priorities, d["priority_id"])
        print(f"[{d['id']}] {mark} {d['title']} | {pname} | {aname} | {prname}")


def main() -> None:
    authors = load_dict(AUTHORS_FILE)
    projects = load_dict(PROJECTS_FILE)
    priorities = load_dict(PRIORITIES_FILE)
    debts = load_list(DEBTS_FILE)

    while True:
        print("\n=== Система учёта технического долга ===")
        print("1.  Показать авторов")
        print("2.  Добавить автора")
        print("3.  Найти автора")
        print("4.  Показать проекты")
        print("5.  Добавить проект")
        print("6.  Найти проект")
        print("7.  Показать приоритеты")
        print("8.  Добавить приоритет")
        print("9.  Показать задачи долга")
        print("10. Добавить задачу")
        print("11. Найти задачу")
        print("12. Задачи проекта")
        print("13. Задачи автора")
        print("14. Задачи по приоритету")
        print("15. Сортировать по приоритету")
        print("16. Закрыть задачу")
        print("17. Удалить задачу")
        print("18. Статистика")
        print("0.  Выход")

        choice = input("Действие: ")

        try:
            if choice == "1":
                show_authors(authors)
            elif choice == "2":
                name = input("Имя: ")
                email = input("Email: ")
                add_author(authors, name, email)
                save_json(AUTHORS_FILE, authors)
                print("Автор добавлен.")
            elif choice == "3":
                q = input("Подстрока: ")
                for aid, a in find_author(authors, q):
                    print(f"[{aid}] {a['name']} — {a['email']}")
            elif choice == "4":
                show_projects(projects)
            elif choice == "5":
                name = input("Название проекта: ")
                desc = input("Описание: ")
                add_project(projects, name, desc)
                save_json(PROJECTS_FILE, projects)
                print("Проект добавлен.")
            elif choice == "6":
                q = input("Подстрока: ")
                for pid, p in find_project(projects, q):
                    print(f"[{pid}] {p['name']}")
            elif choice == "7":
                show_priorities(priorities)
            elif choice == "8":
                name = input("Название приоритета: ")
                w = input_int("Вес (1–5): ")
                try:
                    add_priority(priorities, name, w)
                    save_json(PRIORITIES_FILE, priorities)
                    print("Приоритет добавлен.")
                except ValueError as e:
                    print(f"Ошибка: {e}")
            elif choice == "9":
                show_debts(debts, projects, authors, priorities)
            elif choice == "10":
                title = input("Название задачи: ")
                pid = input_int("ID проекта: ")
                aid = input_int("ID автора: ")
                prid = input_int("ID приоритета: ")
                if pid not in projects or aid not in authors or prid not in priorities:
                    print("Проверьте ID: проект/автор/приоритет не найдены.")
                    continue
                add_debt(debts, title, pid, aid, prid)
                save_json(DEBTS_FILE, debts)
                print("Задача добавлена.")
            elif choice == "11":
                q = input("Подстрока: ")
                show_debts(find_debt(debts, q), projects, authors, priorities)
            elif choice == "12":
                pid = input_int("ID проекта: ")
                show_debts(filter_by_project(debts, pid), projects, authors, priorities)
            elif choice == "13":
                aid = input_int("ID автора: ")
                show_debts(filter_by_author(debts, aid), projects, authors, priorities)
            elif choice == "14":
                prid = input_int("ID приоритета: ")
                show_debts(filter_by_priority(debts, prid), projects, authors, priorities)
            elif choice == "15":
                show_debts(sort_by_priority(debts, priorities), projects, authors, priorities)
            elif choice == "16":
                did = input_int("ID задачи: ")
                if close_debt(debts, did):
                    save_json(DEBTS_FILE, debts)
                    print("Задача закрыта.")
                else:
                    print("Не найдена.")
            elif choice == "17":
                did = input_int("ID задачи: ")
                if delete_debt(debts, did):
                    save_json(DEBTS_FILE, debts)
                    print("Удалена.")
                else:
                    print("Не найдена.")
            elif choice == "18":
                print(statistics(debts))
            elif choice == "0":
                print("Выход.")
                break
            else:
                print("Неверный выбор.")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")


if __name__ == "__main__":
    main()