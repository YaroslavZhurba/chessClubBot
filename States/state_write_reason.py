import reason_handler
import user_handler
import reasons_collection
import tgbot
import users_collection


def process(text, user):
    reason = reason_handler.make_reason(user, text)
    user_chat_id = user_handler.get_chat_id(user)
    tgbot.send_message(user_chat_id, "Весьма жалкая причина!")
    user_handler.set_default_states(user)
    users_collection.add_or_modify_user(user)
    reasons_collection.add_or_modify_reason(reason)
