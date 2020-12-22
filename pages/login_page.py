from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url = str(self.browser.current_url)
        assert "login" in cur_url, "Substring 'login' not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.BLOCK_HEADER), "Block header is not presented"
        assert self.is_element_present(*LoginPageLocators.EMAIL_FORM), "Field 'Email address' is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FORM), "Field 'Password' is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_RESET), "Link 'password reset' is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Log in button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.BLOCK_HEADER_REG), "Block header is not presented"
        assert self.is_element_present(*LoginPageLocators.EMAIL_FORM_REG), "Field 'Email address' is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FORM_REG), "Field 'Password' is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_CONFIRM_FORM_REG), "Field 'Confirm password'" \
                                                                                      " is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Log in button is not presented"

    def register_new_user(self, email, password):
        email_address_field = self.browser.find_element(*LoginPageLocators.EMAIL_FORM_REG)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_REG)
        password_confirmed_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_FORM_REG)
        button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)

        email_address_field.send_keys(email)
        password_field.send_keys(password)
        password_confirmed_field.send_keys(password)
        button.click()
