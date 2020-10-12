import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

#не промо ссылка
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page (browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_can_add_item_to_cart(browser):
    page = ProductPage(browser,link)
    page.open()
    #page.link_is_promo_page() Для заданий с промо
    page.add_item_to_cart()
    #page.solve_quiz_and_get_code() Для заданий с промо
    page.item_added_to_cart_messages()
    page.cart_cost_message()
    page.added_item_name()
    page.added_item_cost()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_item_to_cart()
    #page.solve_quiz_and_get_code() Для заданий с промо
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_dissapeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.add_item_to_cart()
    #page.solve_quiz_and_get_code() Для заданий с промо
    page.should_desappeared_success_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser,link)
    page.open()
    page.go_to_cart()
    page.cart_list_is_empty()
    page.cart_is_empty_message()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(str(time.time()) + "@fakemail.com", "000111aaa") #взамен page.register_new_user

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_item_to_cart(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.add_item_to_cart()
        page.item_added_to_cart_messages()
        page.cart_cost_message()
        page.added_item_name()
        page.added_item_cost()