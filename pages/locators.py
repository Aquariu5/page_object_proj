from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")

class MainPageLocators():
    pass

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.XPATH, "//input[@name = 'registration-email']")
    REGISTER_PASS1 = (By.XPATH, "//input[@name = 'registration-password1']")
    REGISTER_PASS2 = (By.XPATH, "//input[@name = 'registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name = 'registration_submit']")

class ProductLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")


    GOOD_ALERT = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon:nth-child(1)")
    GOOD_NAME_ALERT = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon:nth-child(1) strong")
    GOOD_NAME_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")

    GOOD_PRICE_ALERT = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon:nth-child(3) strong")
    GOOD_PRICE_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color")