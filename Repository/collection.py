import rw
import user_handler
import configs

# local functions and variables
users = None


# read database if needed
def before_users():
    global users
    if users is None:
        users = rw.read_users()


def get_user_index_by_user_chat_id(user_chat_id):
    before_users()
    for i in range(len(users)):
        user = users[i]
        if user_handler.get_user_chat_id(user) == user_chat_id:
            return i
    return None


def get_user_index_by_user_name(user_name):
    before_users()
    for i in range(len(users)):
        user = users[i]
        if user_handler.get_user_name(user) == user_name:
            return i
    return None


# todo check
def add_admin_local(admin_name):
    before_users()
    admin_index = get_user_index_by_user_name(admin_name)
    user_handler.set_user_permission(users[admin_index],configs.admin_permission)


# public functions and variables
def find_user_chat_id_by_user_name(user_name):
    before_users()
    for user in users:
        if user_handler.get_user_name(user) == user_name:
            return user_handler.get_user_chat_id(user)
    return None


def get_all_users():
    before_users()
    return users


def get_all_admins():
    before_users()
    admins = []
    for user in users:
        if user_handler.get_user_permission(user) == configs.admin_permission:
            admins.append(user)
    return admins


def is_user_exists(user_chat_id):
    before_users()
    if get_user_index_by_user_chat_id(user_chat_id) is None:
        return False
    return True


# todo check
def is_admin_exists(admin_chat_id):
    before_users()
    for user in users:
        if user_handler.get_user_chat_id(user) == admin_chat_id and \
                user_handler.get_user_permission(user) == configs.admin_permission:
            return True
    return False


# todo check
# Success -> True
# Failed -> False
def add_admin_by_name(admin_name):
    before_users()
    admin_index = get_user_index_by_user_name(admin_name)
    if admin_index is None:
        return False
    user_handler.set_user_permission(users[admin_index], configs.admin_permission)
    rw.write_users(users)
    return True


# todo rewrite to check success ?
def add_admins_by_name(admin_names):
    before_users()
    for admin_name in admin_names:
        add_admin_local(admin_name)
    rw.write_users(users)


# Success -> True
# Failed (user already exists)-> False
def add_user(chat_id, username):
    before_users()
    if is_user_exists(chat_id):
        return False
    user = {'chat_id': chat_id, 'username': username,
            'permission': configs.user_permission, "state": configs.default_state_id,
            }
    users.append(user)
    rw.write_users(users)
    return True


# Success -> True
# Failed -> False
def remove_admins(admin_names):
    before_users()
    for admin_name in admin_names:
        admin_index = get_user_index_by_user_name(admin_name)
        if admin_index is not None:
            user_handler.set_user_permission(users[admin_index], configs.user_permission)
    rw.write_usesrs(users)
    return True


def is_user_admin(user_chat_id):
    admin_index = get_user_index_by_user_chat_id(user_chat_id)
    if admin_index is not None and user_handler.get_user_permission(users[admin_index]) == configs.admin_permission:
        return True
    return False


# Success -> user
# Failed -> None
def get_user_by_user_chat_id(user_chat_id):
    user_index = get_user_index_by_user_chat_id(user_chat_id)
    if user_index is not None:
        return users[user_index]
    return None


# Success -> user
# Failed -> None
def get_user_by_user_name(user_name):
    user_index = get_user_index_by_user_name(user_name)
    if user_index is not None:
        return users[user_index]
    return None


def add_or_modify_user(user):
    user_chat_id = user_handler.get_user_chat_id(user)
    user_index = get_user_index_by_user_chat_id(user_chat_id)
    if user_index is None:
        users.append(user)
    else:
        user[user_index] = user
    rw.write_users(users)


# var = None
#
#
# def get_var(default_value):
#     global var
#     if var is None:
#         var = default_value
#     return var
#
#
# def set_var(value):
#     global var
#     var = value
