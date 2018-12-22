from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import pyperclip

from time import sleep
import os, sys



class Bot(Chrome):
    def __init__(self):


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
        self.get('http://web.whatsapp.com')
        self.wait_for_page()
        return self
        # 

    def __exit__(self, error_type, value, traceback):
        # print(error_type)
        # print(value)
        # print(traceback)
        global html
        html = self.find_element_by_tag_name("html")

        if not error_type:
            self.close()
            self.quit()
    
    def wait_for_page(self):
        print("waitando")
        while self.find_elements_by_class_name('_2EZ_m'):
            sleep(0.5)

        print("Passou o qr")
        while self.find_elements_by_class_name('Pg7Si'):
            sleep(0.5)

        while not self.find_elements_by_class_name('_2Qffr'):
                print("Sem conexão, tentando novamente...")
                self.get('http://web.whatsapp.com')
                print("getou")
                self.wait_for_page()

        print("passou o load")
        while not self.find_elements_by_class_name('_1vDUw'):
            sleep(0.1)
        print("deu")
    
    @staticmethod
    def clear_console():
        _ = os.system('cls' if os.name=='nt' else 'clear')
        
            
    # def send_keys(element, key, *args):
    #     all_args = (key,) + args
    #     # print(all_args)
    #     element.send_keys(all_args)
    # # def p():
    # #     print(2)


# if __name__ == "__main__":
    # with Bot() as b:

        # with open("whatsapp_load.html")
        # input("1111111111 ")
        # txtBox = b.find_elements_by_class_name('_2S1VP')[0]
        # txtBox.send_keys(1,2,3,4)

        # bot.p()
        # bot.send_keys(Keys.CONTROL, "t")