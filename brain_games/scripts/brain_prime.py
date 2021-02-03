#!/usr/bin/env python
"""Brain entry point."""
from brain_games.cli import welcome_user
from brain_games.game import run
from brain_games.games.prime import get_question_and_answer


def main():
    """Входная точка в Brain."""
    user = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    run(user, get_question_and_answer)


if __name__ == '__main__':
    main()
