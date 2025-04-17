from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

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
        assert self.is_not_element_present(*ProductPageLocators.success_message), \
            ("Success message is presented, but should not be")

    def should_be_message_of_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.success_message), (
            "Element is not desappeared"
        )