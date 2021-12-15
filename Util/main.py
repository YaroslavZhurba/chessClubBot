import telepot
import json
import sys
import os

absolute_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
print(absolute_path)
sys.path.append(absolute_path + '/DataRW')
sys.path.append(absolute_path + '/Handler')
sys.path.append(absolute_path + '/Parser')
print(sys.path)
import rw
import parser
import handler

token = '2091745164:AAEhI5BJicvgcPVxTwpHedFLwha6vSQLbL0'
TelegramBot = telepot.Bot(token)

users = rw.read_users()
admins = rw.read_admins()


def is_admin(chat_id):
    for admin in admins:
        if chat_id == admin['chat_id']:
            return True
    return False


def get_chat_id(update):
    return update['message']['chat']['id']


def get_user_name(update):
    return update['message']['chat']['username']


def find_chat_id(name):
    for user in users:
        if user['username'] == name:
            return user['chat_id']


def is_user_exists(chat_id):
    for user in users:
        if user['chat_id'] == chat_id:
            return True
    return False


def ask_users(names):
    for name in names:
        user_chat_id = find_chat_id(name)
        TelegramBot.sendMessage(user_chat_id, "Че не ходим? + долг по физре")


def get_text_body(command, text):
    return text[len(command) + 1:]


def is_admin_exists(chat_id):
    for admin in admins:
        if admin['chat_id'] == chat_id:
            return True
    return False


def add_admin(names):
    for name in names:
        user_chat_id = find_chat_id(name)
        if not is_admin_exists(user_chat_id):
            admin = {'chat_id': user_chat_id, 'username': name}
            admins.append(admin)


def reply_admin(text, chat_id):
    command = parser.get_command(text)
    if command == 'exit':
        return True
    lst = get_text_body(command, text).split(',')
    if command == 'ask':
        ask_users(lst)
    elif command == 'add_admin':
        #         print(lst)
        add_admin(lst)
    elif command == 'remove_admin':
        remove_admin(lst)
    else:
        TelegramBot.sendMessage(chat_id, rw.say_hello())
    return False


def remove_admin(names):
    for name in names:
        user_chat_id = find_chat_id(name)
        if (is_admin_exists(user_chat_id)):
            admin = {'chat_id': user_chat_id, 'username': name}
            admins.remove(admin)


def get_text(update):
    return update['message']['text']


def add_user(chat_id, username):
    if (is_user_exists(chat_id)):
        return
    usr = {'chat_id': chat_id, 'username': username}
    users.append(usr)


def make_decision(update):
    if update.get('message') is None:
        return False
    chat_id = get_chat_id(update)
    if is_admin(chat_id):
        if reply_admin(get_text(update), chat_id):
            return True
    if get_text(update) == '/start':
        add_user(chat_id, get_user_name(update))
    return False


update_id = 0
while True:
    updates = TelegramBot.getUpdates()
    if len(updates) > 0:
        update_id = updates[0]['update_id']
        break
flag = True
while flag:
    updates = TelegramBot.getUpdates(update_id)
    if len(updates) > 0:
        for update in updates:
            if make_decision(update):
                flag = False
                update_id += len(updates)
                TelegramBot.getUpdates(update_id)
                break
        update_id += len(updates)


rw.write_users(users)
rw.write_admins(admins)

print(admins)
print(users)
