import configs
import quiz_collection
import quiz_results_collections
import rw
import user_handler


def get_chat_id(quiz_result):
    return quiz_result["chat_id"]


def get_quiz_id(quiz_result):
    return quiz_result["quiz_id"]


def get_score(quiz_result):
    return quiz_result["score"]


def set_score(pos, score):
    quiz_results_collections.db[pos]["score"] = score
    rw.write_database(configs.DataBases.quiz_results, quiz_results_collections.db)


def set_zero_score(user_id, quiz_id):
    res, pos = quiz_results_collections.get_by_chat_quiz(user_id, quiz_id)
    set_score(pos, 0)


def add_score(pos):
    set_score(pos, get_score(quiz_results_collections.db[pos]) + 1)
