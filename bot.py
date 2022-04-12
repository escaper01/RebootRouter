from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import json


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        ## make the browser Headless
        option = Options()
        option.headless = True

        _service = Service(executable_path='./geckodriver.exe')
        self.driver = webdriver.Firefox(service=_service, options=option)
        print('headless initialisation was successful')
    
    def rebooting(self, timer= 1):
        self.driver.get("http://192.168.1.1/")
        time.sleep(timer * 4)
        loginBtn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"manage-connected-devices")))
        loginBtn.click()

        username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"f_username")))
        username.clear()
        username.send_keys(self.username)

        password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"f_password")))
        password.clear()
        password.send_keys(self.password)

        submit = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"f_submit_login")))
        submit.click()
        print('Log in')


        time.sleep(timer * 4)
        self.driver.get("http://192.168.1.1/html/reboot.html")
        time.sleep(timer * 4)

        restart = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"span_reboot_apply_button")))
        restart.click()

        confirm = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"pop_confirm")))
        confirm.click()

        print('Router is Restarting...')
        time.sleep(timer * 10)
        self.driver.close()

if __name__ == '__main__':
    with open('credentials.json') as file:
        data = json.load(file)

        myBot = Bot(username=data['username'],
                    password=data["password"])

        myBot.rebooting(timer=2)
        