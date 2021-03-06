import random

from brain_games.engine import run

INTRO = 'What is the result of the expression?'
NUMBER_RANGE = 1, 99
OPERATIONS = ('+', '-', '*')


def calculate_expression(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    raise Exception('Invalid operation "{0}"'.format(operation))


def get_question_and_answer():
    number1 = random.randint(*NUMBER_RANGE)
    number2 = random.randint(*NUMBER_RANGE)
    operation = random.choice(OPERATIONS)
    question = '{0} {1} {2}'.format(number1, operation, number2)
    answer = calculate_expression(number1, number2, operation)
    return question, str(answer)


def run_game():
    run(INTRO, get_question_and_answer)
