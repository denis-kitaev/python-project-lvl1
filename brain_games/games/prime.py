import random

NUMBER_RANGE = 1, 99


def is_prime(number):
    """Является ли число простым."""
    if number > 1:
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True
    return False


def get_is_prime_answer(number):
    return 'yes' if is_prime(number) else 'no'


def get_question_and_answer():
    number = random.randint(*NUMBER_RANGE)
    return number, get_is_prime_answer(number)
