import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    try:
        browser.find_element_by_css_selector("#add_to_basket_form")
        basket_btn = True
        return basket_btn
    except:
        basket_btn = False

    assert basket_btn, 'Button is missing on the page'
