def input_person():
    """Ввод данных о человеке."""
    surname = input("Введите фамилию: ").strip()
    name = input("Введите имя: ").strip()
    zodiac = input("Введите знак Зодиака: ").strip()

    while True:
        try:
            day = int(input("Введите день рождения: ").strip())
            month = int(input("Введите месяц рождения: ").strip())
            year = int(input("Введите год рождения: ").strip())
            if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
                break
            else:
                print("Неверная дата! Повторите ввод.")
        except ValueError:
            print("Введите числа!")

    return {
        "surname": surname,
        "name": name,
        "zodiac": zodiac,
        "birthday": [day, month, year],
    }


def display_person(person):
    """Вывод информации о человеке."""
    print(f"Фамилия: {person['surname']}")
    print(f"Имя: {person['name']}")
    print(f"Знак Зодиака: {person['zodiac']}")
    print(
        f"Дата рождения: {person['birthday'][0]}.{person['birthday'][1]}.{person['birthday'][2]}"
    )
    print("-" * 30)


def find_by_surname(people, surname):
    """Поиск человека по фамилии."""
    results = []
    for person in people:
        if person["surname"].lower() == surname.lower():
            results.append(person)
    return results


def main():
    """Главная функция."""
    people = []

    while True:
        print("\n--- Меню ---")
        print("1. Добавить человека")
        print("2. Вывести всех (по датам рождения)")
        print("3. Найти по фамилии")
        print("4. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            person = input_person()
            people.append(person)
            people.sort(
                key=lambda x: (x["birthday"][2], x["birthday"][1], x["birthday"][0])
            )
            print("Человек добавлен!")

        elif choice == "2":
            if not people:
                print("Список пуст!")
            else:
                print("\nСписок людей (по датам рождения):")
                print("=" * 30)
                for p in people:
                    display_person(p)

        elif choice == "3":
            if not people:
                print("Список пуст! Сначала добавьте людей.")
                continue

            surname = input("Введите фамилию для поиска: ").strip()
            results = find_by_surname(people, surname)

            if results:
                print(f"\nНайдено {len(results)} человек(а):")
                for p in results:
                    display_person(p)
            else:
                print("Человек с такой фамилией не найден!")

        elif choice == "4":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    main()
