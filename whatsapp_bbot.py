import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep

mouse = Controller()

class WhatsApp:
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''
        self.messages = []
        self.sender = ''

    # Navigate to our message input box
    def nav_input_box(self):
        try:
            width, height = pt.size()  # Get the screen size
            center_x, center_y = width // 2, height // 2  # Calculate the center coordinates
            pt.moveTo(center_x-100, center_y+312)  # Move the cursor to the center

            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exeption (nav_message): ', e)

wa_bot = WhatsApp(speed=.5, click_speed=.4)
sleep(20)
wa_bot.nav_input_box()


sleep(20)