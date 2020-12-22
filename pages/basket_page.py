from .base_page import BasePage
from .locators import BasketPageLocators, BasePageLocators


class BasketPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_CART), "There are items in the cart."
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Text is not presented"
