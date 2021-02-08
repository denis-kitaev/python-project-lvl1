import random

INTRO = 'What number is missing in the progression?'
START_ELEMENT_RANGE = 1, 9
STEP_RANGE = 2, 8
LENGTH_RANGE = 5, 10


def get_progression(start, step, length):
    return list(range(start, start + step * length, step))


def get_random_pregression():
    start = random.randint(*START_ELEMENT_RANGE)
    step = random.randint(*STEP_RANGE)
    length = random.randint(*LENGTH_RANGE)
    return get_progression(start, step, length)


def get_question_and_answer():
    progression = get_random_pregression()
    missing_index = random.randint(0, len(progression) - 1)
    answer = progression[missing_index]
    progression[missing_index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(answer)
