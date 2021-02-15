import random

from brain_games.engine import run

INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_RANGE = 1, 99


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    question = random.randint(*NUMBER_RANGE)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer


def run_game():
    run(INTRO, get_question_and_answer)
