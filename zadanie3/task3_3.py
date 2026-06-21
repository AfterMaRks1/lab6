def max_depth(data):
    """Определяет максимальную глубину вложенности списка."""
    if not isinstance(data, list):
        return 0

    if not data:
        return 1

    return 1 + max(max_depth(item) for item in data)


if __name__ == "__main__":
    print(max_depth([1, [2, [3, [4]]]]))  # 4
    print(max_depth([1, 2, [3, 4]]))  # 2
