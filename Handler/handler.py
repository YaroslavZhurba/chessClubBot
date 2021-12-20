import state_write_reason
import users_collection
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
    users_collection.add_or_modify_user(user)
    return True


def user_stop(update):
    user_chat_id = update_handler.get_user_chat_id_stopped(update)
    users_collection.remove_user_by_user_chat_id(user_chat_id)


# todo rewrite
def make_decision(update):
    if update_handler.is_user_stopped_bot(update):
        user_stop(update)
        return

    text = update_handler.get_text(update)
    if text is None:
        return
    user_chat_id = update_handler.get_user_chat_id(update)
    user_name = update_handler.get_user_name(update)
    command, args = parser_bot.get_command_and_args(text)
    if user_start(user_chat_id, user_name, command):
        return

    user = users_collection.get_user_by_user_chat_id(user_chat_id)
    # todo what if user is not in our database
    if user is None:
        return
    user_state = user_handler.get_state(user)

    if user_state == configs.States.default:
        state_default.process(command, args, user)
    elif user_state == configs.States.quiz:
        state_quiz.process(command, args, user)
    elif user_state == configs.States.chess_task:
        state_chess_task.process(command, args, user)
    elif user_state == configs.States.write_reason:
        state_write_reason.process(text, user)


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
