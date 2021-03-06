import quiz_collection
import quiz_results_collections
import quiz_results_handler
import quiz_handler
import reasons_collection
import state_chess_task
import state_quiz
import user_handler
import configs
import users_collection
import tgbot


def list_admins(user_chat_id):
    tgbot.send_message(user_chat_id, "список админов:")
    admins = users_collection.get_all_admins()
    lst = []
    for admin in admins:
        lst.append(user_handler.get_name(admin))
    tgbot.send_message(user_chat_id, str(lst))
    return True


def list_users(user_chat_id):
    tgbot.send_message(user_chat_id, "список пользователей:")
    users = users_collection.get_all_users()
    lst = []
    for user in users:
        lst.append(user_handler.get_name(user))
    tgbot.send_message(user_chat_id, str(lst))
    return True


def ask_users(names, user):
    if user_handler.get_permission(user) != configs.Permissions.admin:
        user_chat_id = user_handler.get_chat_id(user)
        tgbot.send_message(user_chat_id, configs.Messages.no_rights)
        return False
    user_chat_id = user_handler.get_chat_id(user)
    lst = []
    all_right = True
    for name in names:
        user_chat_id = users_collection.find_user_chat_id_by_user_name(name)
        if tgbot.send_message(user_chat_id, configs.Messages.why_no_attendance) is False:
            all_right = False
            lst.append(name)
        else:
            user = users_collection.get_user_by_user_chat_id(user_chat_id)
            user_handler.set_state(user, configs.States.write_reason)
            users_collection.add_or_modify_user(user)
    if all_right is True:
        tgbot.send_message(user_chat_id, "Повистка до всех дошла :)")
    else:
        tgbot.send_message(user_chat_id, "Не до всех дошло, видимо уже не ходят, лови список:")
        tgbot.send_message(user_chat_id, str(lst))
    return True


def make_exit(user, user_chat_id):
    if user_handler.get_permission(user) != configs.Permissions.admin:
        tgbot.send_message(user_chat_id, configs.Messages.no_rights)
        return False
    configs.shutdown = True
    admins = users_collection.get_all_admins()
    for admin in admins:
        admin_chat_id = user_handler.get_chat_id(admin)
        tgbot.send_message(admin_chat_id, configs.Messages.bye_bye)
    return True


def say_hello(user, user_chat_id):
    if user_handler.get_permission(user) != configs.Permissions.admin:
        tgbot.send_message(user_chat_id, configs.Messages.user_greeting)
        return True
    tgbot.send_message(user_chat_id, configs.Messages.admin_greeting)
    return True


def add_admins(args, user_chat_id):
    lst = []
    all_right = True
    for user_name in args:
        if users_collection.add_admin_by_name(user_name) is False:
            all_right = False
            lst.append(user_name)
    if all_right is True:
        tgbot.send_message(user_chat_id, "Всех успешно добавили! А как иначе?)")
    else:
        tgbot.send_message(user_chat_id, "Не всех добавили, думал в сказку попал? Вот список с кем проблемы:")
        tgbot.send_message(user_chat_id, str(lst))
    return True


def remove_admins(args, user_chat_id):
    lst = []
    all_right = True
    for admin_name in args:
        if users_collection.remove_admin_by_name(admin_name) is False:
            all_right = False
            lst.append(admin_name)
    if all_right is True:
        tgbot.send_message(user_chat_id, "Всех успешно удалили! А как иначе?)")
    else:
        tgbot.send_message(user_chat_id, "Не всех удалили, думал в сказку попал? Вот список с кем проблемы:")
        tgbot.send_message(user_chat_id, str(lst))
    return True


def list_reasons(user, user_chat_id):
    if user_handler.get_permission(user) != configs.Permissions.admin:
        tgbot.send_message(user_chat_id, configs.Messages.no_rights)
        return False
    reasons = reasons_collection.get_all_reasons()
    tgbot.send_message(user_chat_id, str(reasons))
    return True


def list_quiz(args, user, user_chat_id):
    if user_handler.get_permission(user) != configs.Permissions.admin:
        tgbot.send_message(user_chat_id, configs.Messages.no_rights)
        return False
    user_res = users_collection.get_user_by_user_name(args[0])
    if user_res is None:
        tgbot.send_message(user_chat_id, "Таких тут нет")
        return False
    user_res_chat_id = user_handler.get_chat_id(user_res)
    quiz_results = quiz_results_collections.get_by_chat_id(user_res_chat_id)
    if quiz_results is None:
        tgbot.send_message(user_chat_id, "Данный студент не писал квизы. Боится наверное!")
        return False
    s = ''
    for res in quiz_results:
        score = quiz_results_handler.get_score(res)
        id = quiz_results_handler.get_quiz_id(res)
        amount = quiz_handler.get_amount(quiz_collection.get_quiz(id))
        s += "quiz_id: " + str(id) + ", score = " + str(score) + "/" + str(amount) + "\n"
    tgbot.send_message(user_chat_id, s)
    return True


def to_quiz(command, args, user):
    user_handler.set_state(user, configs.States.quiz)
    return state_quiz.process(command, args, user)


def to_chess_task(command, args, user):
    user_handler.set_state(user, configs.States.chess_task)
    return state_chess_task.process(command, args, user)


def process(command, args, user):
    user_chat_id = user_handler.get_chat_id(user)
    if command == 'ask':
        return ask_users(args, user)
    elif command == '/list_users':
        return list_users(user_chat_id)
    elif command == '/list_admins':
        return list_admins(user_chat_id)
    elif command == '/list_reasons':
        return list_reasons(user, user_chat_id)
    elif command == 'list_quiz':
        return list_quiz(args, user, user_chat_id)
    elif command == '/exit':
        return make_exit(user, user_chat_id)
    elif command == 'add_admins':
        return add_admins(args, user_chat_id)
    elif command == 'remove_admins':
        return remove_admins(args, user_chat_id)
    elif command == 'quiz':
        return to_quiz(command, args, user)
    elif command == "chess_task":
        return to_chess_task(command, args, user)
    else:
        return say_hello(user, user_chat_id)
