from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import ProductPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find('login') != -1, "Некорректный адрес страницы"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Отсутствует форма авторизации"
        assert self.is_element_present(*LoginPageLocators.LOGIN_LOGIN), "Auth. Отсутствует поле ввода логина"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Auth. Отсутствует поле ввода пароля"
        assert self.is_element_present(*LoginPageLocators.LOGIN_RESET), "Auth. Отсутствует кнопка 'Я забыл пароль'"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Auth. Отсутствует кнопка авторизации"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Отсутствует форма регистрации"
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Reg. Отсутствует поле ввода е-мэйла"
        assert self.is_element_present(*LoginPageLocators.REG_PASS), "Reg. Отсутствует поле ввода пароля"
        assert self.is_element_present(*LoginPageLocators.REG_REPASS), "Reg. Отсутствует поле ввода повторного пароля"
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), "Reg. Отсутствует кнопка регистрации"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_REPASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
    
    def login_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_LOGIN).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()