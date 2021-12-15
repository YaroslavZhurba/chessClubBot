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