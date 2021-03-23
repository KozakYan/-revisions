# здесь находятся алиасы до локаторов
# классы логина и корзины необходимо расскоментировать, когда
# будете писать тесты (нельзя иметь пустой класс)

from selenium.webdriver.common.by import By


Sing_in_objects = {

    'button_sing_in': '//span[text()="Войти"]',

    'input_for_email': '//input[@id="login-entity"]',

    'input_for_password': '//input[@type="password"]',

    'button_submit_for_sing_in': '//input[@value="Войти"]',

    'error_login_notification': '//span[@id="login-password-error"]'
}

LK_objects = {

    'LK_title': '//div[@class="title"]',

    'button_logout': '//a[@id="logout"]'
}

Catalog = {

    'catalog_button': '//button[@class="main-bar__button main-bar__menu-button"]',

    'subcategory_link': '//li[@class="subcategory-item__item"]',

    'product': '//li[@class="_3aKyB"]',

    'button_ad_dto_cart': '//div[@class="_2dEKE _1MxTH"]]'



}

Basket = {

    'basket_button': '//div[@ class="cart-with-popup__wrapper links-group__item"]',


    'block_product': '//div[@ id="row2909410"]',

   'button_delete_product': '//span[@class="with-icon with-icon_x-grey ctl js-ctl-delete set-to-zero"]',

    'basket_cost_block': '//div[@class="b-bill js-b-cart-bill-wrapper"]',

    'empty_cart_text': '//div[@class="empty-cart"]'

}
