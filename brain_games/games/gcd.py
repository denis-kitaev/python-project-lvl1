import random

INTRO = 'Find the greatest common divisor of given numbers.'
NUMBER_RANGE = 1, 99


def get_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def get_question_and_answer():
    num1 = random.randint(*NUMBER_RANGE)
    num2 = random.randint(*NUMBER_RANGE)
    question = '{0} {1}'.format(num1, num2)
    answer = get_gcd(num1, num2)
    return question, str(answer)
