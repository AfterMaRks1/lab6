import os


def walk_dir(path):
    """Рекурсивно обходит каталог и возвращает список всех файлов."""
    files = []
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                files.extend(walk_dir(full_path))
            else:
                files.append(full_path)
    except PermissionError:
        pass
    return files


if __name__ == "__main__":
    print(walk_dir("."))
