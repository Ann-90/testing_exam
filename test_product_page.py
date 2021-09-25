import pytest
import time
from .pages.product_page import ProductPage

links = list(map(
    lambda x: f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{x}', range(0, 10)))

link_invalid = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"


@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.solve_quiz_and_get_code()


@pytest.mark.need_review
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_invalid)
    page.open()
    page.should_be_product_page()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_invalid)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_invalid)
    page.open()
    page.should_be_product_page()
    page.solve_quiz_and_get_code()
    page.is_disappeared()
