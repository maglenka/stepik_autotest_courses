from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasketPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def go_to_empty_basket(self):
        basket_button = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        basket_button.click()
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_CART), "There are items in the cart."
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Text is not presented"
