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
