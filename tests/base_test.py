# запуск и закрытие браузера
# настройки браузера

import unittest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

chromedriver_autoinstaller.install()

class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # headless режим
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-gpu')

        # если не заработает Chrome, переключитесь на FF
        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Firefox()
        self.driver.get("https://sima-land.ru/")

        

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=1).run(suite)
