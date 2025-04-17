from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form > button")
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():

    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_BOOK = (By.XPATH, "//div[@class='col-sm-6 product_main']/child::h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".price_color")
    NAME_BOOK_IN_CART = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_BOOK_IN_CART = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#message .alert:nth-child(1) .alertinner')

