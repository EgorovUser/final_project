from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    LOGIN_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_RESET = (By.CSS_SELECTOR, ".login_form a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login_form .btn")
    REG_FORM = (By.CSS_SELECTOR, ".register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_REPASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, ".register_form .btn")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCES_ADD_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    CART_COST_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
    CART_ADDED_SUMM = (By.CSS_SELECTOR, ".alert-info strong")
    MINI_CART_SUMM = (By.CSS_SELECTOR, ".basket-mini")
    MINI_CART_TEXT = (By.CSS_SELECTOR, ".basket-mini > strong")
    ITEM_PAGE_SUMM = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_MESSAGE_BUTTONS = (By.CSS_SELECTOR, ".alertinner .btn-info")
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    NAME_IN_ITEM = (By.CSS_SELECTOR, ".product_main h1")