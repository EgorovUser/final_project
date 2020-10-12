from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def go_to_cart(self):
        link = self.browser.find_element(*BasePageLocators.GO_TO_CART_BUTTON)
        link.click()

    def cart_list_is_empty(self):
        elements = self.browser.find_elements(*BasePageLocators.CART_ITEMS_ROWS)
        assert len(elements) == 0, "Корзина оказалась не пустой"

    def cart_is_empty_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_CART_MESSAGE), "Сообщения о пустой корзине нет"