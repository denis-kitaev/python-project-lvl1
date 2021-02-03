"""CLI helpers."""
import prompt


def welcome_user() -> str:
    """Prompt user for name and welcome."""
    print('Welcome to the Brain Games!')
    user = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user))
    return user
