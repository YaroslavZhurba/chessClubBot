import rw
import reason_handler
import configs

# local functions and variables
db = None


# read database if needed
def before_reasons():
    global db
    if db is None:
        db = rw.read_database(configs.DataBases.reasons)


def get_reason_index_by_user_chat_id(user_chat_id):
    before_reasons()
    for i in range(len(db)):
        reason = db[i]
        if reason_handler.get_user_chat_id(reason) == user_chat_id:
            return i
    return None


def get_reason_index_by_user_name(user_name):
    before_reasons()
    for i in range(len(db)):
        reason = db[i]
        if reason_handler.get_user_name(reason) == user_name:
            return i
    return None


# public functions
# Success -> reason
# Failed -> None
def get_reason_by_chat_id(user_chat_id):
    reason_index = get_reason_index_by_user_chat_id(user_chat_id)
    if reason_index is not None:
        return db[reason_index]
    return None


# Success -> reason
# Failed -> None
def get_user_by_user_name(user_name):
    reason_index = get_reason_index_by_user_name(user_name)
    if reason_index is not None:
        return db[reason_index]
    return None


def get_all_reasons():
    before_reasons()
    return db


def add_or_modify_reason(reason):
    user_chat_id = reason_handler.get_user_chat_id(reason)
    reason_index = get_reason_index_by_user_name(user_chat_id)
    if reason_index is None:
        db.append(reason)
    else:
        db[reason_index] = reason
    rw.write_database(configs.DataBases.reasons, db)
