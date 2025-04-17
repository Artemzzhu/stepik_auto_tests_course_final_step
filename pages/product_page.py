from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    def add_to_basket_and_get_code(self):
        self.check_name_book()
        self.check_price_book()
        self.go_to_add_to_basket()
        self.solve_quiz_and_get_code()

    def check_name_book(self):
        NAME = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        assert "The shellcoder's handbook" in NAME.text, "There is no name like this"
    def check_price_book(self):
        PRICE = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        assert "9.99" in PRICE.text, "There is no price like this"

    def go_to_add_to_basket(self):
        try:
            BUTTON_ADD_TO_BASKET = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((ProductPageLocators.BUTTON_ADD_TO_BASKET)))
            BUTTON_ADD_TO_BASKET.click()
        except TimeoutException:
            raise AssertionError("Не удалось найти кнопку 'Add to basket' или она не кликабельна")
