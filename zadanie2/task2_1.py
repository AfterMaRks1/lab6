def calc_all(*args, operation="sum"):
    """Вычисляет сумму или произведение всех переданных чисел."""
    if not args:
        return None

    if operation == "sum":
        return sum(args)
    elif operation == "mul":
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return None


if __name__ == "__main__":
    print(calc_all(1, 2, 3, operation="sum"))  # 6
    print(calc_all(2, 3, 4, operation="mul"))  # 24
    print(calc_all())  # None
