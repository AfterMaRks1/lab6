def report(title, *sections, **options):
    """Формирует текст отчёта с заголовком и разделами."""
    if options.get("upper", False):
        title = title.upper()

    separator = options.get("separator", "\n")
    return title + "\n" + separator.join(sections)


if __name__ == "__main__":
    print(
        report("Daily Report", "Sales up", "New clients: 3", separator="\n", upper=True)
    )
