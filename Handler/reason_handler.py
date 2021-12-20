import user_handler


def make_reason(user, text):
    return {"chat_id": user_handler.get_chat_id(user),
            "username": user_handler.get_name(user),
            "text": text}


def get_user_name(reason):
    return reason["username"]


def get_chat_id(reason):
    return reason["chat_id"]


def get_user_reason(reason):
    return reason["text"]


def set_user_name(reason, user_name):
    reason["username"] = user_name


def set_user_chat_id(reason, user_name):
    reason["chat_id"] = user_name


def set_user_reason(reason, text):
    reason["text"] = text
