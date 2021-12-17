import configs


def get_user_name(user):
    return user["username"]


def get_user_permission(user):
    return user["permission"]


def get_user_chat_id(user):
    return user["chat_id"]


def is_user_admin(user):
    return user["permission"] == configs.user_permission


def get_user_state(user):
    return user["state"]


def get_user_substate(user):
    return user["substate"]


def get_user_random_state(user):
    return user["random_state"]