# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

import telepot
import json

token = '2091745164:AAEhI5BJicvgcPVxTwpHedFLwha6vSQLbL0'
TelegramBot = telepot.Bot(token)

# users = [{'chat_id': 399682596, 'username' : 'Yaroslav239'}]
f = open('database.txt', 'r')
users = json.loads(f.read())
f.close()
f = open('admins.txt', 'r')
admins = json.loads(f.read())
f.close()


def is_admin(chat_id):
    for admin in admins:
        if chat_id == admin['chat_id']:
            return True
    return False


def get_chat_id(update):
    return update['message']['chat']['id']


def get_user_name(update):
    return update['message']['chat']['username']


# make_admin
def get_command(text):
    if text[0:3] == 'ask':
        return 'ask'
    if text[0:9] == 'add_admin':
        return 'add_admin'
    if text[0:12] == 'remove_admin':
        return 'remove_admin'
    if text[0:4] == 'exit':
        return 'exit'
    return 'hello'


def find_chat_id(name):
    for user in users:
        if (user['username'] == name):
            return user['chat_id']


def is_user_exists(chat_id):
    for user in users:
        if (user['chat_id'] == chat_id):
            return True
    False


def ask_users(names):
    for name in names:
        user_chat_id = find_chat_id(name)
        TelegramBot.sendMessage(user_chat_id, "Че не ходим? + долг по физре")


def get_text_body(command, text):
    return text[len(command) + 1:]


def is_admin_exists(chat_id):
    for admin in admins:
        if (admin['chat_id'] == chat_id):
            return True
    False


def add_admin(names):
    for name in names:
        user_chat_id = find_chat_id(name)
        if (not is_admin_exists(user_chat_id)):
            admin = {'chat_id': user_chat_id, 'username': name}
            admins.append(admin)


def reply_admin(text, chat_id):
    command = get_command(text)
    if (command == 'exit'):
        return True
    lst = get_text_body(command, text).split(',')
    if (command == 'ask'):
        ask_users(lst)
    elif (command == 'add_admin'):
        #         print(lst)
        add_admin(lst)
    elif (command == 'remove_admin'):
        remove_admin(lst)
    else:
        TelegramBot.sendMessage(chat_id, "Здоров, командир! Че делаем?")
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
    if update.get('message') == None:
        return False
    chat_id = get_chat_id(update)
    if is_admin(chat_id):
        if (reply_admin(get_text(update), chat_id)):
            return True
    if get_text(update) == '/start':
        add_user(chat_id, get_user_name(update))
    return False


update_id = 0
while True:
    updates = TelegramBot.getUpdates()
    if (len(updates) > 0):
        update_id = updates[0]['update_id']
        break
flag = True
while flag:
    updates = TelegramBot.getUpdates(update_id)
    if (len(updates) > 0):
        for update in updates:
            if (make_decision(update)):
                flag = False
                update_id += len(updates)
                TelegramBot.getUpdates(update_id)
                break
        update_id += len(updates)

# update = {'update_id': 108826025,
#   'message': {'message_id': 339,
#    'from': {'id': 168224409,
#     'is_bot': False,
#     'first_name': 'Анастасия 🌅',
#     'username': 'HACTEHbKA',
#     'language_code': 'ru'},
#    'chat': {'id': 168224409,
#     'first_name': 'Анастасия 🌅',
#     'username': 'HACTEHbKA',
#     'type': 'private'},
#    'date': 1636057214,
#    'text': '/start',
#    'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}]}}
# make_decision(update)


f = open('database.txt', 'w')
f.write(json.dumps(users))
f.close()
f = open('admins.txt', 'w')
f.write(json.dumps(admins))
f.close()

print(admins)
print(users)