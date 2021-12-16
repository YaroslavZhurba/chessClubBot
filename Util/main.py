import telepot
import json
import sys
import os

absolute_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
print(absolute_path)
sys.path.append(absolute_path + '/DataRW')
sys.path.append(absolute_path + '/Handler')
sys.path.append(absolute_path + '/Parser')
sys.path.append(absolute_path + '/Repository')
print(sys.path)
import handler

handler.run()
# while True:
#     updates = TelegramBot.getUpdates()
#     if len(updates) > 0:
#         update_id = updates[0]['update_id']
#         break
# flag = True
# while flag:
#     updates = TelegramBot.getUpdates(update_id)
#     if len(updates) > 0:
#         for update in updates:
#             if handler.make_decision(update):
#                 flag = False
#                 update_id += len(updates)
#                 TelegramBot.getUpdates(update_id)
#                 break
#         update_id += len(updates)
