import random

INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUMBER_RANGE = 1, 99


def is_prime(number):
    """Является ли число простым."""
    if number <= 1:
        return False
    if number == 2:
        return True

    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            return False
    return True


def get_is_prime_answer(number):
    return 'yes' if is_prime(number) else 'no'


def get_question_and_answer():
    number = random.randint(*NUMBER_RANGE)
    answer = get_is_prime_answer(number)
    return number, answer
