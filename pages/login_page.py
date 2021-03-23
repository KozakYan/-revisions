# здесь описываете методы, которые можно использовать на странице логина

from pages.base_page import BasePage
from utils.locators import *

class LoginPage(BasePage):
    def log_out(self):
        self.driver.get(config.links['lk_link'])
        button_logout = driver.find_element_by_xpath(locators.LK_objects['button_logout'])
        button_logout.click()
        button_sing_in.click()
        input_for_email.is_displayed()