import collection
import parser_bot
import state_chess_task
import state_default
import state_quiz
import update_handler
import tgbot
import configs
import user_handler


# command == "/start" -> True
# else -> False
def user_start(user_chat_id, user_name, command):
    if command != "/start":
        return False
    user = user_handler.make_default_user_by_user_chat_id_and_name(user_chat_id, user_name)
    collection.add_or_modify_user(user)
    return True
# True -> continue working
# False -> shutdown
# def reply_admin(text, user_chat_id):
#     command, args = parser.get_command_and_args(text)
#     if command == 'exit':
#         return False
#     if command == 'ask':
#         ask_users(args)
#     elif command == 'add_admins_by_name':
#         collection.add_admins_by_name(args)
#     elif command == 'remove_admins':
#         collection.remove_admins(args)
#     elif command == 'list_admins':
#         list_admins(user_chat_id)
#     elif command == 'list_users':
#         list_users(user_chat_id)
#     else:
#         tgbot.send_message(user_chat_id, configs.admin_greeting)
#     return True


# todo rewrite
def make_decision(update):
    text = update_handler.get_text(update)
    if text is None:
        return
    user_chat_id = update_handler.get_user_chat_id(update)
    user_name = update_handler.get_user_name(update)
    command, args = parser_bot.get_command_and_args(text)
    if user_start(user_chat_id, user_name, command):
        return

    user = collection.get_user_by_user_chat_id(user_chat_id)
    # todo what if user is not in our database
    if user is None:
        return
    user_state = user_handler.get_user_state(user)

    # switch
    if user_state == configs.default_state_id:
        state_default.process(command, args, user)
    elif user_state == configs.quiz_state_id:
        state_quiz.process(command, args, user)
    elif user_state == configs.chess_task_state_id:
        state_chess_task.process(command, args, user)



def process(updates):
    for update in updates:
        make_decision(update)


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
        process(updates)
        if configs.shutdown is True:
            break
    tgbot.shutdown()
    # print(str(updates))
