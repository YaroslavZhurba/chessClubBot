import rw

# local functions and variables
users = None
admins = None


def before_admins():
    global admins
    if admins is None:
        admins = rw.read_admins()


def before_users():
    global users
    if users is None:
        users = rw.read_users()


def add_admin_local(admin_name):
    user_chat_id = find_user_chat_id(admin_name)
    if not is_admin_exists(user_chat_id):
        admin = {'chat_id': user_chat_id, 'username': admin_name}
        admins.append(admin)


# public functions and variables
def find_user_chat_id(name):
    before_users()
    for user in users:
        if user['username'] == name:
            return user['chat_id']
    return None


def get_all_users():
    before_users()
    return users


def get_all_admins():
    before_admins()
    return admins


def is_user_exists(chat_id):
    before_users()
    for user in users:
        if user['chat_id'] == chat_id:
            return True
    return False


def is_admin_exists(chat_id):
    before_admins()
    for admin in admins:
        if admin['chat_id'] == chat_id:
            return True
    return False


def add_admin(admin_name):
    before_admins()
    user_chat_id = find_user_chat_id(admin_name)
    if not is_admin_exists(user_chat_id):
        admin = {'chat_id': user_chat_id, 'username': admin_name}
        admins.append(admin)


def add_admins(admin_names):
    before_admins()
    for admin_name in admin_names:
        add_admin_local(admin_name)
    rw.write_admins(admins)


def add_user(chat_id, username):
    before_users()
    if is_user_exists(chat_id):
        return
    user = {'chat_id': chat_id, 'username': username}
    users.append(user)
    rw.write_users(users)


def remove_admins(admin_names):
    before_admins()
    for admin_name in admin_names:
        user_chat_id = find_user_chat_id(admin_name)
        if is_admin_exists(user_chat_id):
            admin = {'chat_id': user_chat_id, 'username': admin_name}
            admins.remove(admin)
    rw.write_admins(admins)


def is_user_admin(chat_id):
    before_admins()
    for admin in admins:
        if chat_id == admin['chat_id']:
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
