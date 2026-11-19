def normalize_city(value: str) -> str:
    """Basic baseline: trim surrounding whitespace only."""
    return value.strip()


def parse_amount(value: str) -> float | None:
    """Basic baseline: cannot yet handle thousand separators or nonpositive values."""
    try:
        return float(value.strip())
    except ValueError:
        return None
