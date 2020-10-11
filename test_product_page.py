import pytest
import time
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_link_is_promo(browser):
    page = ProductPage(browser,link)
    page.open()
    page.link_is_promo_page()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    #time.sleep(180)
    page.item_added_to_cart_messages()
    page.cart_cost_message()
    page.added_item_name()
    page.added_item_cost()