import sys
import os

absolute_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
print(absolute_path)
sys.path.append(absolute_path + '/DataRW')
sys.path.append(absolute_path + '/Handler')
sys.path.append(absolute_path + '/Parser')
sys.path.append(absolute_path + '/Repository')
sys.path.append(absolute_path + '/States')
print(sys.path)
import handler
import user_handler

handler.run()
# user = {"chat_id": 399682596, "username": "Yaroslav239", "permission" : 1, "state" : 0, "substate" : 0, "random_state" : 0}
# user_handler.set_user_state(user, 1)
# print(user)
