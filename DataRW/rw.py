import os
import json


def get_path_to_database() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)) + "/DataBase/"


def read_database(name):
    f = open(get_path_to_database() + name, 'r', encoding='utf8')
    result = json.loads(f.read())
    f.close()
    return result


def write_database(name, data):
    f = open(get_path_to_database() + name, 'w', encoding='utf8')
    f.write(json.dumps(data, ensure_ascii=False))
    f.close()
    return
