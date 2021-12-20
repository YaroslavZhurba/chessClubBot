import questions_collection
import rw
import user_handler
import configs
import users_collection
import tgbot

# local functions and variables
db = None


# read database if needed
def before_quizzes():
    global db
    if questions_collection.db is None:
        questions_collection.questions = rw.read_database(configs.DataBases.questions)
    if db is None:
        db = rw.read_database(configs.DataBases.quiz)
        db["amount"] = len(db["quizzes"])


def get_quizzes_amount():
    before_quizzes()
    return db["amount"]


def get_quizzes():
    before_quizzes()
    return db["quizzes"]


def get_quiz(id):
    before_quizzes()
    quizzes = get_quizzes()
    return quizzes[id]


def get_user_quiz(user):
    before_quizzes()
    quizzes = get_quizzes()
    return quizzes[user_handler.get_random_state(user)]
