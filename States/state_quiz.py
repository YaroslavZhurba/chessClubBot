import quiz_handler
import quiz_results_collections
import quiz_results_handler
import user_handler
import question_handler
import configs
import users_collection
import tgbot
import random
import quiz_collection
import questions_collection


def check_answer(user, command):
    question = question_handler.get_question_by_user(user)
    return command == question_handler.get_correct_answer(question)


def send_question(user, amount):
    question = question_handler.get_question_by_user(user)
    answers = question_handler.get_answer_for_message(question)
    substate = user_handler.get_substate(user)
    return tgbot.send_message(user_handler.get_chat_id(user),
                              "Вопрос №" + str(substate + 1) + "/" + str(amount) + ":\n" +
                              question_handler.get_question(question) + "\n" + answers)


def start_quiz(user):
    quiz_collection.before_quizzes()
    user_handler.set_state(user, configs.States.quiz)
    user_handler.set_substate(user, 0)
    quiz_no = random.randint(0, quiz_collection.db["amount"] - 1)
    user_handler.set_random_state(user, quiz_no)
    quiz = quiz_collection.db["quizzes"][quiz_no]
    quiz_results_handler.set_zero_score(user_handler.get_chat_id(user), quiz_no)
    return send_question(user, quiz_handler.get_amount(quiz))


def continue_quiz(user, command):
    quiz_result, pos = quiz_results_collections.get_by_chat_quiz(user_handler.get_chat_id(user),
                                                                 quiz_handler.get_id(
                                                                     quiz_collection.get_user_quiz(user)))
    if check_answer(user, command):
        quiz_results_handler.add_score(pos)

    substate = user_handler.get_substate(user) + 1
    user_handler.set_substate(user, substate)
    quiz = quiz_collection.get_user_quiz(user)

    if quiz_handler.get_amount(quiz) == substate:
        return end_quiz(user, quiz_results_handler.get_score(quiz_result), substate)
    return send_question(user, quiz_handler.get_amount(quiz))


def end_quiz(user, quiz_result, max_result):
    user_handler.set_state(user, configs.States.default)
    return tgbot.send_message(user_handler.get_chat_id(user),
                              "Результат: " + str(quiz_result) + " из " + str(max_result))


def process(command, args, user):
    if command == 'quiz':
        return start_quiz(user)
    else:
        return continue_quiz(user, command)
