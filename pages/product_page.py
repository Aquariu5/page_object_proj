from .base_page import BasePage
from .locators import ProductLocators

class ProductPage(BasePage):
    def go_to_good_page(self):
        login_link = self.browser.find_element(*ProductLocators.ADD_TO_BASKET)
        login_link.click()

    def should_be_add_basket_link(self):
        assert self.is_element_present(*ProductLocators.ADD_TO_BASKET), "Add to basket is not presented"

    def should_be_same_good_name(self):
        assert self.is_element_present(*ProductLocators.GOOD_NAME_ALERT), "Alert good name not found"
        assert self.is_element_present(*ProductLocators.GOOD_NAME_PAGE), "Good name goodsPage not found"

        alert = self.browser.find_element(*ProductLocators.GOOD_NAME_ALERT).text
        main = self.browser.find_element(*ProductLocators.GOOD_NAME_PAGE).text
        assert  alert == main
        print("Same names in goods")

    def should_be_same_good_prices(self):
        assert self.is_element_present(*ProductLocators.GOOD_PRICE_ALERT), "Alert good name not found"
        assert self.is_element_present(*ProductLocators.GOOD_PRICE_PAGE), "Good name goodsPage not found"

        alert = self.browser.find_element(*ProductLocators.GOOD_NAME_ALERT).text
        main = self.browser.find_element(*ProductLocators.GOOD_NAME_PAGE).text
        assert  alert == main
        print("Same prices in goods")
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductLocators.GOOD_ALERT), \
        "Success message is presented, but should not be"

    def should_not_be_dissapeared_success_message(self):
        assert self.is_disappeared(*ProductLocators.GOOD_ALERT), \
        "Success message is dissapeared, but should not be"
