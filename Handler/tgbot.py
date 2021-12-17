import telepot

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


def send_message(user_chat_id, message):
    TelegramBot.sendMessage(user_chat_id, message)
