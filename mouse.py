from pynput import mouse, keyboard
import math

totaldist = 0
lastpos = None
running = True
dpi = 96
#conversion values
pixtoinch = 1 / dpi
inchtom= 0.0254
inchtofeet = 1 / 12

def move(x, y): 
    global totaldist, lastpos
    if lastpos is not None:
        x_i, y_i = lastpos
        dist = math.sqrt((x - x_i) ** 2 + (y - y_i) ** 2)#using distance formula to find pixels moves
        totaldist += dist
    lastpos = (x, y)

def press(key): 
    global running
    try:
        if key.char == 'a':
            running = False
            return False 
    except AttributeError:
        pass #to check for other keys

def calc():
    totalinch = totaldist * pixtoinch
    totalm= totalinch * inchtom
    totalfeet = totalinch * inchtofeet
    return totalinch, totalfeet, totalm

def tracker(): 
    global runninga
    mouse_listener = mouse.Listener(on_move=move)
    mouse_listener.start()
    with keyboard.Listener(on_press=press) as klistener:
        print("Tracking mouse distance. Press 'A' to stop.")
        while running:
            pass

    mouse_listener.stop()

tracker()
totalinch, totalfeet, totalm = calc()
print(f"\nYour mouse has travelled a distance of: {totalinch:.2f} inches, {totalfeet:.2f} feet, {totalm:.2f} meters.")
print("Exiting....")
