#!/usr/bin/env python
"""Brain Progression entry point."""
from brain_games.game import run
from brain_games.games.progression import INTRO, get_question_and_answer


def main():
    """Входная точка в Brain Progression."""
    run(INTRO, get_question_and_answer)


if __name__ == '__main__':
    main()
