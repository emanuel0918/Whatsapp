import pyautogui as pt
import pyperclip as pc
import urllib.parse
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

    # Main function
    def process(self):
        self.nav_input_box()
        try:
            position = pt.locateOnScreen('C:\\Users\\Emanuel\\WhatsappBot\\env\\green_dot_ss.png',confidence=0.8)
            if position is not None :
                pt.moveTo(position[0:2], duration=self.speed)
                pt.moveRel(-100,0,self.speed)
                pt.click()
                print(' get new messages at ',position)
                
                self.get_messages()

        except Exception as e:
            print('Exeption (nav_green_dot): ', e)


    # Check all the messages kept in a range of 3 seconds
    def get_messages(self):
        count = 0
        while count < 5 :
            self.nav_message()
            self.get_message()
            sleep(1)
            count = count +1
        print('The big message was \n')
        for encodedString in self.messages :
            print(encodedString)

    # Copies the message that we want to process
    def get_message(self):
        mouse.click(Button.left,3)
        sleep(self.speed)
        mouse.click(Button.right,1)
        sleep(self.speed)
        width, height = pt.size()  # Get the screen size
        center_x, center_y = width // 2, height // 2  # Calculate the center coordinates
        pt.moveTo(center_x-200, center_y+80)
        pt.moveRel(10,10,duration=self.speed)
        mouse.click(Button.left,1)
        sleep(1)

        self.message = pc.paste()
        if self.message != self.last_message :
            print('The user \'TEST1\' says: ', self.message)
            self.messages.append(urllib.quote_plus(self.message))
        else :
            if self.last_message == '' :
                print('The user \'TEST1\' says: ', self.message)
                self.messages.append(urllib.quote_plus(self.message))
        self.last_message = self.message


    # Naviagtes to the message we want to respond to
    def nav_message (self):
        try:
            width, height = pt.size()  # Get the screen size
            center_x, center_y = width // 2, height // 2  # Calculate the center coordinates
            pt.moveTo(center_x-200, center_y+255)  # Move the cursor to the center



            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exeption (nav_message): ', e)

    # Navigate to our message input box
    def nav_input_box(self):
        try:
            width, height = pt.size()  # Get the screen size
            center_x, center_y = width // 2, height // 2  # Calculate the center coordinates
            pt.moveTo(center_x-100, center_y+312)  # Move the cursor to the center

            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exeption (nav_message): ', e)

    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('green_dot.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100,0,self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exeption (nav_green_dot): ', e)

wa_bot = WhatsApp(speed=.5, click_speed=.4)
sleep(5)
# esto debe estar en un ciclo
#wa_bot.nav_green_dot()
# validar que si se este leyendo un mensaje nuevo y si 
# no existe flujo no terminar el proceso

#wa_bot.process()


contador = 1
while contador < 15:
    contador = contador + 1
    wa_bot.process()
    sleep(1)

#wa_bot.nav_input_box()
sleep(20)