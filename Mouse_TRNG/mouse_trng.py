from ctypes import windll, Structure, c_long, byref
import json
import time

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

mouse_list = []

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return [pt.x, pt.y]


pos = queryMousePosition()
# time.sleep(0.1)

mouse_list.append(pos)
while 1:
    pos = queryMousePosition()
    #time.sleep(0.1)
    if pos == mouse_list[-1]:
        continue
    time.sleep(0.1)
    mouse_list.append(pos)
    print(len(mouse_list))
    if len(mouse_list) == 300000:
        break




with open('plik3.json','w') as plik:
    json.dump(mouse_list,plik)


