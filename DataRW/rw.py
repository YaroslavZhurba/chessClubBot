import os
import json


def get_path_to_database() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)) + "/DataBase"


def user_database_name() -> str:
    return '/database.txt'


# def admin_database_name() -> str:
#     return '/admins.txt'


def read_users():
    f = open(get_path_to_database() + user_database_name(), 'r')
    result = json.loads(f.read())
    f.close()
    return result


# def read_admins():
#     f = open(get_path_to_database() + admin_database_name(), 'r')
#     result = json.loads(f.read())
#     f.close()
#     return result


def write_users(users):
    f = open(get_path_to_database() + user_database_name(), 'w')
    f.write(json.dumps(users))
    f.close()
    return


# def write_admins(admins):
#     f = open(get_path_to_database() + admin_database_name(), 'w')
#     f.write(json.dumps(admins))
#     f.close()
#     return
