# здесь описываете методы, которые можно использовать на странице корзины

from pages.base_page import BasePage
from utils.locators import *

class CartPage(BasePage):
    def __init__(self, driver):
        self.locator = CartPageLocators
        super().__init__(driver)

     def delete_product(self):
        button_delete_product = driver.find_element_by_xpath(locators.Basket['button_delete_product'])
        button_delete_product.click()

    def check_the_item_in_the_cart(self):
        block_product = driver.find_element_by_xpath(locators.Basket['basket_cost_block'])
        block_product.is_displayed()