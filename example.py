import sys
from datetime import date


def display_workers(staff):
    """Отобразить список работников в виде таблицы."""
    if not staff:
        print("Список работников пуст.")
        return

    line = "+" + "-" * 4 + "+" + "-" * 30 + "+" + "-" * 20 + "+" + "-" * 8 + "+"

    print(line)
    print(
        "| {:^4} | {:^30} | {:^20} | {:^8} |".format("", "Ф.И.О.", "Должность", "Год")
    )
    print(line)

    for idx, worker in enumerate(staff, 1):
        print(
            "| {:>4} | {:<30} | {:<20} | {:>8} |".format(
                idx,
                worker.get("name", ""),
                worker.get("post", ""),
                worker.get("year", 0),
            )
        )
    print(line)


def get_worker():
    """Запросить данные о работнике у пользователя."""
    name = input("Введите Ф.И.О. работника: ").strip()
    post = input("Введите должность: ").strip()
    while True:
        year_str = input("Введите год приёма на работу: ").strip()
        try:
            year = int(year_str)
            if year <= 0 or year > date.today().year:
                print("Год должен быть положительным и не больше текущего.")
                continue
            break
        except ValueError:
            print("Год должен быть числом.")
    return {"name": name, "post": post, "year": year}


def select_workers(staff, period):
    """Выбрать работников с заданным стажем."""
    today = date.today()
    result = []
    for employee in staff:
        emp_year = employee.get("year", today.year)
        if today.year - emp_year >= period:
            result.append(employee)
    return result


def show_menu():
    """Показать стартовое меню."""
    print("=" * 50)
    print("ДОБРО ПОЖАЛОВАТЬ В ПРОГРАММУ УЧЁТА СОТРУДНИКОВ")
    print("=" * 50)
    print("\nДоступные команды:")
    print("  add     - добавить работника")
    print("  list    - вывести список работников")
    print("  select  - запросить работников со стажем не менее указанного")
    print("  help    - отобразить справку")
    print("  exit    - завершить работу с программой")
    print("\n" + "=" * 50)
    print("Введите команду и нажмите Enter\n")


def main():
    """Главная функция программы."""
    workers = []

    # Показываем стартовое меню
    show_menu()

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            worker = get_worker()
            workers.append(worker)
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get("name", ""))

        elif command == "list":
            display_workers(workers)

        elif command.startswith("select "):
            parts = command.split(" ", maxsplit=1)
            if len(parts) != 2:
                print("Ошибка: укажите стаж после команды select, например: select 5")
                continue
            try:
                period = int(parts[1])
                if period < 0:
                    print("Стаж не может быть отрицательным.")
                    continue
            except ValueError:
                print("Стаж должен быть числом.")
                continue
            selected = select_workers(workers, period)
            display_workers(selected)

        elif command == "help":
            print("Список команд:\n")
            print("add – добавить работника;")
            print("list – вывести список работников;")
            print("select <стаж> – запросить работников со стажем не менее указанного;")
            print("help – отобразить справку;")
            print("exit – завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
