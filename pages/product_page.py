from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.BUTTON_ADD_TO_BASKET = None
        self.SUCCESS_MESSAGE = None

    def add_to_basket_and_get_code(self):
        self.go_to_add_to_basket()
        self.solve_quiz_and_get_code()
        self.check_name_book()
        self.check_price_book()

    def go_to_add_to_basket(self):
        try:
            BUTTON_ADD_TO_BASKET = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((ProductPageLocators.BUTTON_ADD_TO_BASKET)))
            BUTTON_ADD_TO_BASKET.click()
        except TimeoutException:
            raise AssertionError("Не удалось найти кнопку 'Add to basket' или она не кликабельна")

    def check_name_book(self):
        NAME = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        NAME_IN_CART = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_CART)
        print(str(NAME.text) + "-----" + str(NAME_IN_CART.text))
        assert NAME.text in NAME_IN_CART.text, "Значение в корзине и в названии не совпадают"

    def check_price_book(self):
        PRICE = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        PRICE_IN_CART = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_IN_CART)
        print(str(PRICE.text) + "-----" + str(PRICE_IN_CART.text))
        assert PRICE.text in PRICE_IN_CART.text, "Цена в корзине не соответствует цене товара"

    def should_be_message_about_success(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            ("Success message is presented, but should not be")

    def should_be_message_of_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Element is not desappeared"
        )

    def should_be_product_added_to_basket(self):
        self.should_be_correct_product_name()
        self.should_be_correct_basket_total()

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == message_name, \
            f"Product name doesn't match. Expected: {product_name}, got: {message_name}"

    def should_be_correct_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        assert product_price == basket_total, \
            f"Basket total doesn't match product price. Expected: {product_price}, got: {basket_total}"

    def add_to_basket(self):
        # Клик по кнопке добавления товара в корзину
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_button.click()

    def should_not_be_success_message(self):
        # Проверка отсутствия сообщения об успехе
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

