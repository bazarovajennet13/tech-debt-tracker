"""Вспомогательные функции ввода."""


def input_int(prompt: str) -> int:
    """Запросить целое число с повторным вводом."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")