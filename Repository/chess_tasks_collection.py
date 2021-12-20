import questions_collection
import rw
import user_handler
import configs
import users_collection
import tgbot

# local functions and variables
db = None


# read database if needed
def before_chess_tasks():
    global db
    if db is None:
        db = rw.read_database(configs.DataBases.chess_tasks)
        db["amount"] = len(db["tasks"])


def get_amount():
    before_chess_tasks()
    return db["amount"]


def get_tasks():
    before_chess_tasks()
    return db["tasks"]
