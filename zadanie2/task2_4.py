def merge_profiles(*profiles, **defaults):
    """Объединяет профили пользователей с приоритетом последнего."""
    result = {}

    # Сначала добавляем значения по умолчанию
    result.update(defaults)

    # Затем добавляем все профили (последний имеет приоритет)
    for profile in profiles:
        if isinstance(profile, dict):
            result.update(profile)

    return result


if __name__ == "__main__":
    result = merge_profiles(
        {"name": "Alice", "city": "Paris"}, {"age": 25}, country="France"
    )
    print(result)
