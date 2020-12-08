from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_product_to_basket(self):
        product_page_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        product_page_button.click()
        time.sleep(1)
        BasePage.solve_quiz_and_get_code(self)
        time.sleep(3)

    def check_alert_content(self):
        name_of_book = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_CATALOGUE).text
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_IN_CATALOGUE).text

        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_IN_ALERT), "The message is not displayed."
        alert_name_of_book = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_ALERT).text
        assert alert_name_of_book == name_of_book, "The name of the product in the message does not match " \
                                                   "the product you actually added"

        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_IN_ALERT), "The message is not displayed."
        alert_price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_IN_ALERT).text
        assert alert_price_of_book == price_of_book, "Cart value does not match the product price"
