import user_handler
import configs
import collection
import tgbot


def list_admins(user_chat_id):
    tgbot.send_message(user_chat_id, "список админов:")
    admins = collection.get_all_admins()
    for admin in admins:
        tgbot.send_message(user_chat_id, admin["username"])
    return True


def list_users(user_chat_id):
    tgbot.send_message(user_chat_id, "список пользователей:")
    users = collection.get_all_users()
    for user in users:
        tgbot.send_message(user_chat_id, user["username"])
    return True


def ask_users(names, user):
    if user_handler.get_user_permission(user) != configs.admin_permission:
        user_chat_id = user_handler.get_user_chat_id(user)
        tgbot.send_message(user_chat_id, configs.no_rights)
        return False
    for name in names:
        user_chat_id = collection.find_user_chat_id_by_user_name(name)
        tgbot.send_message(user_chat_id, configs.why_no_attendance)
    return True


def make_exit(user, user_chat_id):
    if user_handler.get_user_permission(user) != configs.admin_permission:
        tgbot.send_message(user_chat_id, configs.no_rights)
        return False
    configs.shutdown = True
    tgbot.send_message(user_chat_id, configs.bye_bye)
    return True


def say_hello(user, user_chat_id):
    if user_handler.get_user_permission(user) != configs.admin_permission:
        tgbot.send_message(user_chat_id, configs.user_greeting)
        return True
    tgbot.send_message(user_chat_id, configs.admin_greeting)
    return True


def process(command, args, user):
    user_chat_id = user_handler.get_user_chat_id(user)
    if command == 'ask':
        return ask_users(args, user)
    elif command == 'list_users':
        return list_users(user_chat_id)
    elif command == 'list_admins':
        return list_admins(user_chat_id)
    elif command == 'exit':
        return make_exit(user, user_chat_id)
    else:
        return say_hello(user, user_chat_id)


