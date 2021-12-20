import configs
import quiz_results_handler
import rw

# local functions and variables
db = None


# read database if needed
def before_quiz_results():
    global db
    if db is None:
        db = rw.read_database(configs.DataBases.quiz_results)


def get_by_chat_quiz(chat_id, quiz_id):
    before_quiz_results()
    f = False
    for i in range(len(db)):
        result = db[i]
        if quiz_results_handler.get_chat_id(result) == chat_id and quiz_results_handler.get_quiz_id(result) == quiz_id:
            f = True
            return result, i
    db.append({"chat_id": chat_id, "quiz_id": quiz_id, "score": 0})
    rw.write_database(configs.DataBases.quiz_results, db)
    return db[-1], len(db) - 1


def get_by_chat_id(chat_id):
    before_quiz_results()
    lst = []
    f = False
    for res in db:
        if quiz_results_handler.get_chat_id(res) == chat_id:
            f = True
            lst.append(res)
    if f is False:
        return None
    return lst
