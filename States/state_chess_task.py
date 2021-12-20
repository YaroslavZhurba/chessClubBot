import random

import chess_tasks_collection
import chess_tasks_handler
import configs
import user_handler
import tgbot


def send_task(user):
    chess_task_no = random.randint(0, chess_tasks_collection.get_amount() - 1)
    user_handler.set_random_state(user, chess_task_no)
    task = chess_tasks_handler.get_task(chess_task_no)
    return tgbot.send_photo(user_handler.get_chat_id(user), chess_tasks_handler.get_name(task), chess_tasks_handler.get_message(task))


def check_task(user, command):
    task = chess_tasks_handler.get_task(user_handler.get_random_state(user))
    message = configs.Messages.ChessTasksAnswers.incorrect
    if command == chess_tasks_handler.get_answer(task):
        message = configs.Messages.ChessTasksAnswers.correct
    user_handler.set_state(user, configs.States.default)
    return tgbot.send_message(user_handler.get_chat_id(user), message)


def process(command, args, user):
    if command == "chess_task":
        return send_task(user)
    else:
        return check_task(user, command)
