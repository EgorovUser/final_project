from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def link_is_promo_page(self):
        assert self.browser.current_url.find('promo') != -1, "Страница промо акции не была открыта"
    
    def add_item_to_cart(self):
        assert self.try_click_element(*ProductPageLocators.ADD_TO_CART_BUTTON), "Кнопка добавления в корзину не найдена"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def item_added_to_cart_messages(self):
        message = self.browser.find_elements(*ProductPageLocators.SUCCES_ADD_MESSAGE)
        assert len(message) > 0, "Не найдено сообщение об успешной покупке"
        assert len(message) == 2, "Нет сообщения об акционной покупке"

    def cart_cost_message(self):
        assert self.is_element_present(*ProductPageLocators.CART_COST_MESSAGE), "Сообщение о полносй стоимости корзины не найдено"
        buttons = self.browser.find_elements(*ProductPageLocators.CART_MESSAGE_BUTTONS)
        assert len(buttons) == 2, f"В сообщении о стоимости корзины должны быть 2 кнопки, а сейчас {len(buttons)}"

    def added_item_name(self):
        messages = self.browser.find_elements(*ProductPageLocators.NAME_IN_MESSAGE)
        item_name = self.browser.find_element(*ProductPageLocators.NAME_IN_ITEM)
        names = []
        for name in messages:
            names.append(name.text)
        assert item_name.text in names, f"Название предмета не совпадает с названием из карточки ({item_name.text})"

    def added_item_cost(self):
        mini_cart = self.browser.find_element(*ProductPageLocators.MINI_CART_SUMM)
        mini_cart_text = self.browser.find_element(*ProductPageLocators.MINI_CART_TEXT)
        mini_cart_summ = mini_cart.text.replace(mini_cart_text.text,'')
        mini_cart_summ = mini_cart_summ[0:mini_cart_summ.index('\n')]
        added_summ = self.browser.find_element(*ProductPageLocators.CART_ADDED_SUMM)
        item_summ = self.browser.find_element(*ProductPageLocators.ITEM_PAGE_SUMM)
        assert added_summ.text.replace(' ','') == item_summ.text.replace(' ',''), f"Суммы покупок различаются, нужная - {item_summ.text}, в сообщении - {added_summ.text}"
        assert mini_cart_summ.replace(' ','') == item_summ.text.replace(' ',''), f"Суммы покупок различаются, нужная - {item_summ.text}, в мини-корзине - {mini_cart_summ}"
