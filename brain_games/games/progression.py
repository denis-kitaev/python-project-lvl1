import random

START_ELEMENT_RANGE = 1, 9
STEP_RANGE = 2, 8
COUNT_RANGE = 5, 10


def get_pregression():
    start = random.randint(*START_ELEMENT_RANGE)
    step = random.randint(*STEP_RANGE)
    count = random.randint(*COUNT_RANGE)
    return list(range(start, start + step * count, step))


def get_question_and_answer():
    progression = get_pregression()
    missing_index = random.randint(0, len(progression) - 1)
    answer = progression[missing_index]
    progression[missing_index] = '..'
    return ' '.join(map(str, progression)), answer
