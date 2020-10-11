from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM =(By.CSS_SELECTOR, ".login_form")
    LOGIN_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_RESET = (By.CSS_SELECTOR, ".login_form a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login_form .btn")
    REG_FORM = (By.CSS_SELECTOR, ".register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_REPASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, ".register_form .btn")
