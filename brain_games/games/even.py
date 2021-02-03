import random

NUMBER_RANGE = 1, 99


def get_is_even_answer(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def get_question_and_answer():
    number = random.randint(*NUMBER_RANGE)
    return number, get_is_even_answer(number)
