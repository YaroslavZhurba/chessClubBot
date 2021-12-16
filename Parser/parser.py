def metrics(text):
    if text[0:3] == 'ask':
        return 'ask'
    if text[0:10] == 'add_admins':
        return 'add_admins'
    if text[0:13] == 'remove_admins':
        return 'remove_admins'
    if text[0:4] == 'exit':
        return 'exit'
    if text[0:11] == 'list_admins':
        return 'list_admins'
    if text[0:10] == 'list_users':
        return 'list_users'
    return 'hello'


def get_command(text):
    return metrics(text)


def get_text_body(command, text):
    return text[len(command) + 1:]