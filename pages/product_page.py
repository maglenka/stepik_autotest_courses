from .base_page import BasePage
from .locators import ProductPageLocators, BasketPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        product_page_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        product_page_button.click()
        BasePage.solve_quiz_and_get_code(self)

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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def go_to_empty_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_CART), "There are items in the cart."
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Text is not presented"
