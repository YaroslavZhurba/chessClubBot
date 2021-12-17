import collection
import parser
import update_handler
import tgbot
import configs


def ask_users(names):
    for name in names:
        user_chat_id = collection.find_user_chat_id(name)
        tgbot.send_message(user_chat_id, configs.why_no_attendance)


def list_admins(user_chat_id):
    tgbot.send_message(user_chat_id, "список админов:")
    admins = collection.get_all_admins()
    for admin in admins:
        tgbot.send_message(user_chat_id, admin["username"])


def list_users(user_chat_id):
    tgbot.send_message(user_chat_id, "список пользователей:")
    users = collection.get_all_users()
    for user in users:
        tgbot.send_message(user_chat_id, user["username"])


# True -> continue working
# False -> shutdown
def reply_admin(text, user_chat_id):
    command, args = parser.get_command_and_args(text)
    if command == 'exit':
        return False
    if command == 'ask':
        ask_users(args)
    elif command == 'add_admins_by_name':
        collection.add_admins_by_name(args)
    elif command == 'remove_admins':
        collection.remove_admins(args)
    elif command == 'list_admins':
        list_admins(user_chat_id)
    elif command == 'list_users':
        list_users(user_chat_id)
    else:
        tgbot.send_message(user_chat_id, configs.admin_greeting)
    return True


# True -> continue working
# False -> shutdown
def make_decision(update):
    if update_handler.is_update_has_message(update) is False:
        return True

    user_chat_id = update_handler.get_user_chat_id(update)

    if collection.is_user_admin(user_chat_id) and not reply_admin(update_handler.get_text(update), user_chat_id):
        return False
    if update_handler.get_text(update) == '/start':
        collection.add_user(user_chat_id, update_handler.get_user_name(update))
    return True


# True -> continue working
# False -> shutdown
def process(updates):
    continue_working = True
    for update in updates:
        if make_decision(update) is False:
            continue_working = False
    return continue_working


def run():
    while True:
        if tgbot.init_update_id():
            break

    while True:
        updates = tgbot.get_updates()
        # print(str(updates))
        # tgbot.shutdown()
        if updates is None:
            continue
        if process(updates) is False:
            break
    tgbot.shutdown()
    # print(str(updates))
