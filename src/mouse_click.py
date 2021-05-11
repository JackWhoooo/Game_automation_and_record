import threading
import time

import pydirectinput
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Button, Controller

delay = 0.0
button = Button.right
start_stop_key = KeyCode(char='c')
exit_key = KeyCode(char='v')

pydirectinput.PAUSE = 0


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                # pydirectinput.keyDown('w')
                # pydirectinput.keyUp('w')
                pydirectinput.mouseDown()
                time.sleep(0.01)
                pydirectinput.mouseUp()
                time.sleep(0.01)
            time.sleep(0.05)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
