"""CLI helpers."""
import prompt


def welcome_user() -> str:
    """Prompt user for name."""
    return prompt.string('May I have your name? ')
