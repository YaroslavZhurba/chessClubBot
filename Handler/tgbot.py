import telepot
import configs

token = '2091745164:AAEhI5BJicvgcPVxTwpHedFLwha6vSQLbL0'
TelegramBot = telepot.Bot(token)
update_id = None


def init_update_id() -> bool:
    global update_id
    if update_id is not None:
        return True
    updates = TelegramBot.getUpdates()
    if len(updates) > 0:
        update_id = updates[0]['update_id']
        configs.shutdown = False
        return True
    return False


def get_updates():
    global update_id
    updates = TelegramBot.getUpdates(update_id)
    if len(updates) > 0:
        update_id += len(updates)
        return updates
    return None


def shutdown():
    global update_id
    TelegramBot.getUpdates(update_id)


# Success -> True
# Forbidden -> False
def send_message(user_chat_id, message):
    try:
        TelegramBot.sendMessage(user_chat_id, message)
        return True
    except Exception as e:
        return False


# Success -> True
# Forbidden -> False
def send_photo(user_chat_id, abs_path, message=''):
    try:
        TelegramBot.sendPhoto(user_chat_id, photo=open(abs_path, 'rb'), caption=message)
        return True
    except Exception as e:
        return False
