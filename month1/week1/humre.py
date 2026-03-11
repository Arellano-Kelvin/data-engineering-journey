import re


def num(text: str) -> str | None:
    """Return the first number found in the text as a string."""
    match = re.search(r"\d+", text)
    return match.group(0) if match else None


def name(text: str) -> str | None:
    """Return the name at the start of a 'Name, email, phone' string."""
    # Assume the name is before the first comma
    parts = text.split(",", 1)
    return parts[0].strip() if parts else None


def email(text: str) -> str | None:
    """Return the first email address found in the text."""
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return match.group(0) if match else None


def phone(text: str) -> str | None:
    """Return the first phone number found in the text."""
    match = re.search(r"\d{3}-\d{3}-\d{4}", text)
    return match.group(0) if match else None

