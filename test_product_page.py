import pytest
import time
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.skip
def test_add_promo_item_to_cart(browser):
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

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_item_to_cart()
    #page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_dissapeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_item_to_cart()
    #page.solve_quiz_and_get_code()
    page.should_desappeared_success_message()