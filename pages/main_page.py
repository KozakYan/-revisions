# здесь описываете методы, которые можно использовать на главной

from pages.base_page import BasePage
from utils.locators import *

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def check_mainpage_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False
        
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

        def sing_in(self):
        button_sing_in = driver.find_element_by_xpath(locators.Sing_in_objects['button_sing_in'])
        button_sing_in.click()
        time.sleep(1)
        input_for_email = driver.find_element_by_xpath(locators.Sing_in_objects['input_for_email'])
        input_for_email.send_keys(config.authorization_data['email'])
        input_for_password = driver.find_element_by_xpath(locators.Sing_in_objects['input_for_password'])
        input_for_password.send_keys(config.authorization_data['password'])
        button_submit_for_sing_in = driver.find_element_by_xpath(locators.Sing_in_objects['button_submit_for_sing_in'])
        button_submit_for_sing_in.click()
        time.sleep(1)
        button_sing_in = driver.find_element_by_xpath(locators.Sing_in_objects['button_sing_in'])
        button_sing_in.click()
        time.sleep(2)
        LK_title = driver.find_element_by_xpath(locators.LK_objects['LK_title'])
        LK_title.is_displayed()