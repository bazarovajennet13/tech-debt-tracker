"""Сохранение и загрузка данных в JSON."""

import json
import os


def load_json(filename: str, default):
    """Загрузить JSON или вернуть значение по умолчанию."""
    if not os.path.exists(filename):
        return default
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Ошибка чтения {filename}. Использую значение по умолчанию.")
        return default


def save_json(filename: str, data) -> None:
    """Сохранить данные в JSON."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_dict(filename: str) -> dict:
    """Загрузить словарь id -> данные (ключи в int)."""
    data = load_json(filename, {})
    return {int(k): v for k, v in data.items()}


def load_list(filename: str) -> list:
    """Загрузить список."""
    return load_json(filename, [])