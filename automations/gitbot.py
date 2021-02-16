#!/usr/bin/python3

""" Test script for github login """

from selenium import webdriver

class GithubBot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://github.com")
    
    def login(self, username, password):
        self._username = username
        self._password = password
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(self._username)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self._password)
        self.driver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[14]').click()
        print("Quit Driver")
        self.driver.quit()


if __name__=='__main__':
    import os

    from dotenv import load_dotenv
    load_dotenv(override=True)

    g_bot = GithubBot()
    g_bot.login(os.environ.get('USERNAME'), os.environ.get('PASSWORD'))
