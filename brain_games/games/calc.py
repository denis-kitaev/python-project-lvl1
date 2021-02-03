import random

NUMBER_RANGE = 1, 99
OPS = ('+', '-', '*')


def get_currect_answer(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    return num1 * num2


def get_question_and_answer():
    num1 = random.randint(*NUMBER_RANGE)
    num2 = random.randint(*NUMBER_RANGE)
    op = random.choice(OPS)
    return (
        '{0} {1} {2}'.format(num1, op, num2),
        get_currect_answer(num1, num2, op),
    )
