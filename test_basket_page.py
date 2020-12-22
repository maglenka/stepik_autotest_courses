from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


def test_guest_can_see_empty_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/basket/"
    page = BasketPage(browser, link)
    page.open()
    BasketPage.basket_should_be_empty(page)


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/basket/"
    page = BasketPage(browser, link)
    page.open()
    BasketPage.go_to_login_page(page)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/basket/"
    page = BasketPage(browser, link)
    page.open()
    BasketPage.should_be_login_link(page)
