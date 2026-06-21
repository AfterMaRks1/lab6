def flatten(data):
    """Рекурсивно выравнивает список любой вложенности."""
    result = []

    for item in data:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


if __name__ == "__main__":
    print(flatten([1, [2, [3, 4], 5]]))  # [1, 2, 3, 4, 5]
