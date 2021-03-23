# здесь описываете методы, которые можно использовать везде

class BasePage(object):
    def __init__(self, driver, base_url='https://www.sima-land.ru/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

     def add_product_to_cart(self):
        self.driver.get(config.links['main_page'])
        catalog_button = driver.find_element_by_xpath(locators.Catalog['catalog_button'])
        catalog_button.click()
        subcategory_link = driver.find_element_by_xpath(locators.Catalog['subcategory_link'])
        subcategory_link.clik()
        product = driver.find_element_by_xpath(locators.Catalog['product'])
        product.clik()
        button_ad_dto_cart = driver.find_element_by_xpath(locators.Catalog['button_ad_dto_cart'])
        button_ad_dto_cart.click()
        basket_button = driver.find_element_by_xpath(locators.Basket['product'])
        basket_button.click()
