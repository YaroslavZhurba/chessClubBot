# local functions
def is_update_has_message(update):
    if update.get('message') is not None:
        return True
    return False


# public functions
# Success -> text
# Failed -> None
def get_text(update):
    if is_update_has_message(update) is False:
        return None
    return update['message']['text']


def get_user_name(update):
    return update['message']['chat']['username']


def get_user_chat_id(update):
    return update['message']['chat']['id']


def is_user_stopped_bot(update):
    if update.get('my_chat_member') is None:
        return False
    if update['my_chat_member'].get('new_chat_member') is None:
        return False
    if update['my_chat_member']['new_chat_member']['status'] == 'kicked':
        return True
    return False


def get_user_chat_id_stopped(update):
    return update['my_chat_member']['chat']['id']