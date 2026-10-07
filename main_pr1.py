

project_name: str = "Backend API"
debt_title: str = "Отсутствуют тесты для модуля оплаты"

impact: int = 4       # влияние 
urgency: int = 3      # срочность 
complexity: int = 2   # сложност
files_count: int = 7  # сколько файлов затронет
days_left: int = 10   #  срок


def calculate_priority_score(impact: int, urgency: int) -> int:
    """Вернуть балл приоритета задачи (от 2 до 10)."""
    return impact + urgency 


def estimate_fix_time(complexity: int, files_count: int) -> float:
    """Вернуть оценку времени исправления задачи в часах."""
    base_hours = complexity * 2
    file_hours = files_count * 0.5
    return base_hours + file_hours


def get_debt_status(priority_score: int, days_left: int) -> str:
    """Вернуть текстовый статус задачи долга."""
    if priority_score >= 8 and days_left <= 5:
        return "Критично, исправлять срочно"
    if priority_score >= 6 and days_left <= 10:
        return "Высокий приоритет"
    if priority_score >= 4:
        return "Средний приоритет"
    return "Низкий приоритет"


def main() -> None:
    """Точка входа: вывести отчёт по одной задаче долга."""
    priority_score = calculate_priority_score(impact, urgency)
    estimated_hours = estimate_fix_time(complexity, files_count)
    status = get_debt_status(priority_score, days_left)

    print("=" * 45)
    print("СИСТЕМА УЧЁТА ТЕХНИЧЕСКОГО ДОЛГА")
    print("=" * 45)
    print(f"Проект:        {project_name}")
    print(f"Задача:        {debt_title}")
    print(f"Влияние:       {impact}")
    print(f"Срочность:     {urgency}")
    print(f"Сложность:     {complexity}")
    print(f"Файлов:        {files_count}")
    print(f"Дней до срока: {days_left}")
    print("-" * 45)
    print(f"Балл приоритета: {priority_score}")
    print(f"Оценка времени:  {estimated_hours:.1f} ч")
    print(f"Статус задачи:   {status}")
    print("=" * 45)


if __name__ == "__main__":
    main()