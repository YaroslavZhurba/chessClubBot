import rw
import user_handler
import configs

# local functions and variables
users = None


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


# todo rewrite ???
def add_admin_local(admin_name):
    before_users()
    admin_index = get_user_index_by_user_name(admin_name)
    users[admin_index]["permission"] = configs.admin_permission


# public functions and variables
def find_user_chat_id(user_name):
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


# todo rewrite ??
def is_admin_exists(admin_chat_id):
    before_users()
    for user in users:
        if user_handler.get_user_chat_id(user) == admin_chat_id and \
                user_handler.get_user_permission(user) == configs.admin_permission:
            return True
    return False


def add_admin_by_name(admin_name):
    before_users()
    admin_index = get_user_index_by_user_name(admin_name)
    users[admin_index]["permission"] = configs.admin_permission
    rw.write_users(users)


def add_admins_by_name(admin_names):
    before_users()
    for admin_name in admin_names:
        add_admin_local(admin_name)
    rw.write_users(users)


def add_user(chat_id, username):
    before_users()
    if is_user_exists(chat_id):
        return
    user = {'chat_id': chat_id, 'username': username,
            'permission' : configs.user_permission, "state" : configs.default_state_id,
            }
    users.append(user)
    rw.write_users(users)


def remove_admins(admin_names):
    before_users()
    for admin_name in admin_names:
        admin_index = get_user_index_by_user_name(admin_name)
        if admin_index is not None:
            users[admin_index]["permission"] = configs.user_permission
    rw.write_usesrs(users)


def is_user_admin(user_chat_id):
    admin_index = get_user_index_by_user_chat_id(user_chat_id)
    if admin_index is not None and user_handler.get_user_permission(users[admin_index]) == configs.admin_permission:
        return True
    return False

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
