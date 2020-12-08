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


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "form#add_to_basket_form button.btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME_IN_CATALOGUE = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRICE_IN_CATALOGUE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    BOOK_NAME_IN_ALERT = (By.CSS_SELECTOR, "div.alertinner strong")
    PRICE_IN_ALERT = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in div.alertinner p strong")
