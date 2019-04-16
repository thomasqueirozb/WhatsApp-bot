#!/usr/bin/env python3
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import pyperclip

from time import sleep
import os



class Bot(Chrome):

    '''
    All elements types referenced in the help functions are selenium.webdriver.remote.webelement.WebElement
    '''

    ############
    # Adaptação#
    ############

    def __init__(self):
        '''
        A better adaptation to selenium's standard way of creating a browser
        '''
        self.element = None
        options = Options()
        options.add_argument("--disable-extensions")
        if os.name == "posix":
            try:
                file_name = "./chromedriver_linux"
            except WebDriverException:
                file_name = "./chromedriver_mac"
        else:
            file_name = "./chromedriver.exe"

        super().__init__(file_name, options=options)

    def __enter__(self):
        '''
        Called when entering the with statement

        Makes the browser go to http://web.whatsapp.com and wait for the page to load
        '''

        self.get('http://web.whatsapp.com')
        self.wait_for_page()
        return self

    def __exit__(self, error_type=None, value=None, traceback=None):
        '''
        Called when exiting the with statement

        Closes the browser only if there are no errors (mostly for debugging)
        '''

        if not error_type: 
            self.close()
            self.quit()

    def wait_for_page(self):
        '''
        This function is called when entering the with statement right after http://web.whatsapp.com is entered.
        It exits only when the QR code and the loading screen are not on the page.
        It also refreshed the page if the connection is lost.

        The intervals between checks are 500ms, which should be adequate considering how slow the whatsapp web servers are.
        '''
        # print("waitando")
        while self.find_elements_by_class_name('_2EZ_m'):
            sleep(0.5)

        # print("Passou o qr")
        while self.find_elements_by_class_name('Pg7Si'):
            sleep(0.5)

        while not self.find_elements_by_class_name('_2Qffr'):
            print("Sem conexão, tentando novamente...")
            self.get('http://web.whatsapp.com')
            self.wait_for_page()

        # print("passou o load")
        while not self.find_elements_by_class_name('_1vDUw'):
            sleep(0.1)
        # print("deu")

    #############
    # Essenciais#
    #############

    @staticmethod
    def clear_console():
        '''
        This function clears the console (solely used for visual purposes)
        '''
        _ = os.system('cls' if os.name=='nt' else 'clear')

    @staticmethod
    def copy_to_cipboard(text):
        '''
        This function copies text to the clipboard in order to make writing text easier and faster
        '''
        pyperclip.copy(text)

    #############################################
    # Funções usando um elemento como referência#
    #############################################

    @staticmethod
    def write_copied_message_element(element):
        '''
        Writes text on the clipboard to an element
        '''
        element.send_keys(Keys.CONTROL, 'v')

    def send_copied_message_element(self, element):
        '''
        Writes text on the clipboard to an element and hits the enter key
        '''
        self.write_copied_message_element(element)
        element.send_keys(Keys.ENTER)


    def write_message_element(self, element, text):
        '''
        Copies the text to the clipboard and then writes it to an element
        '''
        self.copy_to_cipboard(text)
        self.write_copied_message_element(element)

    def send_message_element(self, element, text):
        '''
        Copies the text to the clipboard then writes it to an element and hits the enter key
        '''
        self.copy_to_cipboard(text)
        self.send_copied_message_element(element)

    @staticmethod
    def write_message_keys_element(element, text):
        '''
        Writes text to an element by simulating keystrokes

        Note: this the slowest function to write to an element and should only be used if the others fail
        '''
        element.send_keys(text)

    def send_message_keys_element(self, element, text):
        '''
        Writes text to an element by simulating keystrokes and hits the enter key

        Note: this the slowest function to write to an element and should only be used if the others fail
        '''
        self.write_message_keys_element(element, text)
        element.send_keys(Keys.ENTER)

    # def 

    # def send_copied_message(self):
    #     self.element.



    # def find(self):

    #     pass

# Search bar loading icon class_name = _2xarx


if __name__ == "__main__":
    pass
    # with Bot() as b:

        # with open("whatsapp_load.html")
        # input("1111111111 ")
        # txtBox = b.find_elements_by_class_name('_2S1VP')[0]
        # txtBox.send_keys(1,2,3,4)

        # bot.p()
        # bot.send_keys(Keys.CONTROL, "t")
