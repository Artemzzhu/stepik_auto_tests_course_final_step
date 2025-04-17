from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form > button")
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form > button")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_BOOK = (By.XPATH, "//div[@class='col-sm-6 product_main']/child::h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".price_color")
    NAME_BOOK_IN_CART = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
class ProductPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form > button")
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form > button")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_BOOK = (By.XPATH, "//div[@class='col-sm-6 product_main']/child::h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".price_color")
    NAME_BOOK_IN_CART = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert-success strong")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")