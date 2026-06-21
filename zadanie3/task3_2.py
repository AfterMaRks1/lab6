def sierpinski(n):
    """Выводит треугольник Серпинского глубиной n."""
    if n == 1:
        return ["*"]
    else:
        prev = sierpinski(n - 1)
        spaces = " " * (2 ** (n - 2))
        top = [spaces + line + spaces for line in prev]
        bottom = [line + " " + line for line in prev]
        return top + bottom


if __name__ == "__main__":
    for line in sierpinski(4):
        print(line)
