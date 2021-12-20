def get_command(text):
    return text.lstrip().split().pop()


def get_command_and_args(text):
    lst = text.lstrip().split()
    command = lst.pop(0)
    args = ''.join(lst).split(',')
    return command, args


def get_text_body(command, text):
    return text[len(command) + 1:]
