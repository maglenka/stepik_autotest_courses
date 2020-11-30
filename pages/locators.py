from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    BLOCK_HEADER = (By.CSS_SELECTOR, "form#login_form h2")
    EMAIL_FORM = (By.CSS_SELECTOR, "form#login_form input#id_login-username")
    PASSWORD_FORM = (By.CSS_SELECTOR, "form#login_form input#id_login-password")
    PASSWORD_RESET = (By.CSS_SELECTOR, "form#login_form a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "form#login_form button")

    BLOCK_HEADER_REG = (By.CSS_SELECTOR, "form#register_form h2")
    EMAIL_FORM_REG = (By.CSS_SELECTOR, "form#register_form input#id_registration-email")
    PASSWORD_FORM_REG = (By.CSS_SELECTOR, "form#register_form input#id_registration-password1")
    PASSWORD_CONFIRM_FORM_REG = (By.CSS_SELECTOR, "form#register_form input#id_registration-password2")
    REGISTER_BUTTON_REG = (By.CSS_SELECTOR, "form#register_form button")

    CUR_URL = By.current_url
