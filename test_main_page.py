import pytest
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser,link)
    page.open()
    page.go_to_login_page() 

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_login_form(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    time.sleep(3)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart()
    page.cart_list_is_empty()
    page.cart_is_empty_message()
