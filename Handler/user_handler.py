import configs


def make_default_user_by_user_chat_id_and_name(user_chat_id, user_name):
    user = {"chat_id": user_chat_id, "username": user_name, "permission": configs.user_permission,
            "state": configs.default_state_id, "substate": configs.default_substate_id,
            "random_state": configs.default_random_state_id}
    return user


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


def set_user_permission(user, permission_id):
    user["permission"] = permission_id


def set_user_state(user, state_id):
    user["state"] = state_id


def set_user_substate(user, substate_id):
    user["substate"] = substate_id


def set_user_random_state(user, random_state_id):
    user["random_state"] = random_state_id


def set_user_default_states(user):
    set_user_state(user, configs.default_state_id)
    set_user_substate(user, configs.default_substate_id)
    set_user_random_state(user, configs.default_random_state_id)
