import chess_tasks_collection


def get_task(pos):
    return chess_tasks_collection.get_tasks()[pos]


def get_name(task):
    return task["name"]


def get_message(task):
    return task["message"]


def get_answer(task):
    return task["answer"]
