def get_text(update):
    return update['message']['text']


def get_user_name(update):
    return update['message']['chat']['username']


def get_user_chat_id(update):
    return update['message']['chat']['id']


def is_update_has_message(update):
    if update.get('message') is not None:
        return True
    return False
