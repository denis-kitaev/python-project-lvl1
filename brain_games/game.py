import prompt


def run(user, get_question_and_answer_fn):
    """Запуск основного цикла игры."""
    correct_answer_count = 0
    while correct_answer_count < 3:
        question, answer = get_question_and_answer_fn()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(answer):
            print('Correct!')
            correct_answer_count += 1
        else:
            error_msg = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
            print(error_msg.format(user_answer, answer))
            print("Let's try again, {user}!".format(user=user))
            return
    print('Congratulations, {user}!'.format(user=user))
