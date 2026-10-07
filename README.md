# Система учёта технического долга

Консольное приложение для учёта задач технического долга в IT-проектах (ООП-версия).

## Возможности
- учёт авторов, проектов, приоритетов и задач долга;
- поиск, фильтрация, сортировка;
- закрытие и удаление задач;
- статистика;
- хранение данных в JSON.

## Основные классы

### Author — автор задачи
- атрибуты: `id`, `name`, `email`
- методы: `__init__`, `__str__`, `from_data`, `to_data`

### Project — проект
- атрибуты: `id`, `name`, `description`
- методы: `__init__`, `__str__`, `from_data`, `to_data`

### Priority — приоритет задачи
- атрибуты: `id`, `name`, `weight`
- методы: `__init__`, `__str__`, `from_data`, `to_data`

### Debt — задача долга
- атрибуты: `id`, `title`, `project`, `author`, `priority`, `is_closed`
- методы: `__init__`, `close`, `__str__`, `from_data`, `to_data`

## Взаимодействие объектов
`Debt` хранит ссылки на `Project`, `Author` и `Priority`. Это позволяет обращаться к данным связанных объектов напрямую: `debt.project.name`, `debt.author.email`, `debt.priority.weight`.

## Структура проекта
- `main.py` — точка входа;
- `models/` — классы и функции работы с ними;
- `storage.py` — JSON ↔ объекты;
- `utils.py` — ввод;
- `data/` — JSON-файлы;
- `tests/` — автотесты.

## Запуск
```bash
python main.py