import prompt

from brain_games.cli import welcome_user

REQUIRED_CURRECT_ANSWER_COUNT = 3


def run(game_intro, get_question_and_answer):
    """Запуск основного цикла игры."""
    user = welcome_user()
    print(game_intro)

    correct_answer_count = 0
    while correct_answer_count < REQUIRED_CURRECT_ANSWER_COUNT:
        question, answer = get_question_and_answer()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            correct_answer_count += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                user_answer, answer,
            ))
            print("Let's try again, {user}!".format(user=user))
            return

    print('Congratulations, {user}!'.format(user=user))
