import configs


def make_default_user_by_user_chat_id_and_name(user_chat_id, user_name):
    user = {"chat_id": user_chat_id, "username": user_name, "permission": configs.Permissions.user,
            "state": configs.States.default, "substate": configs.Substates.default,
            "random_state": configs.RandomStates.default}
    return user


def get_name(user):
    return user["username"]


def get_permission(user):
    return user["permission"]


def get_chat_id(user):
    return user["chat_id"]


def is_admin(user):
    return user["permission"] == configs.Permissions.user


def get_state(user):
    return user["state"]


def get_substate(user):
    return user["substate"]


def get_random_state(user):
    return user["random_state"]


def set_permission(user, permission_id):
    user["permission"] = permission_id


def set_state(user, state_id):
    user["state"] = state_id


def set_substate(user, substate_id):
    user["substate"] = substate_id


def set_random_state(user, random_state_id):
    user["random_state"] = random_state_id


def set_default_states(user):
    set_state(user, configs.States.default)
    set_substate(user, configs.Substates.default)
    set_random_state(user, configs.RandomStates.default)
