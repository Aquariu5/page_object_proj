from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()