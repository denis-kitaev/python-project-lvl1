#!/usr/bin/env python
"""Brain Games entry point."""
from brain_games.cli import welcome_user


def main():
    """Входная точка в Brain Games."""
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Hello, {name}!'.format(name=name))


if __name__ == '__main__':
    main()
