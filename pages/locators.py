from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a.btn.btn-default")


class LoginPageLocators:
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


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "form#add_to_basket_form button.btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME_IN_CATALOGUE = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRICE_IN_CATALOGUE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    BOOK_NAME_IN_ALERT = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in "
                                           "div.alertinner strong")
    PRICE_IN_ALERT = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in div.alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alert-success")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a.btn.btn-default")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "div #content_inner p")
    ITEM_IN_CART = (By.CSS_SELECTOR, "div.content div#content_inner div.basket-title")
