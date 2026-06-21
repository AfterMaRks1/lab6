def log_event(event_type, *messages, **options):
    """Выводит сообщения лога в формате [LEVEL] (SOURCE) — MESSAGE."""
    level = options.get("level", "INFO")
    source = options.get("source", "SYSTEM")

    for message in messages:
        print(f"[{level}] ({source}) — {message}")


if __name__ == "__main__":
    log_event("start", "Initialization complete", level="DEBUG", source="Core")
