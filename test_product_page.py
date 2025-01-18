import random
import time

import pytest
from selenium import webdriver
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        loginPage = LoginPage(browser, browser.current_url)
        email = str(time.time()) + '@ya.ru'
        passwd = str(random.randint(100000000, 999999999))
        loginPage.register_new_user(email, passwd)
        page.should_be_logout_link()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_logout_link()
        page.go_to_good_page()
        page.should_be_same_good_name()
        page.should_be_same_good_prices()

class TestProductPageGuest:
    @pytest.mark.parametrize('promo', list(range(1)))
    @pytest.mark.skip
    def test_guest_can_go_to_good_page(self, browser, promo):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.should_be_add_basket_link()
        page.go_to_good_page()          # выполняем метод страницы — переходим на страницу логина
        page.solve_quiz_and_get_code() # solve alert
        page.should_be_same_good_name()
        page.should_be_same_good_prices()

        page.should_not_be_success_message()
        page.should_not_be_dissapeared_success_message()

    @pytest.mark.xfail
    def test_not_exist_success_message_after_add_in_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.should_be_add_basket_link()
        page.go_to_good_page()          #
        page.should_be_same_good_name()
        page.should_be_same_good_prices()

        page.should_not_be_success_message()


    def test_not_exist_success_message_after_visit_good_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.should_be_add_basket_link()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_not_dissapeared_success_message_after_add_in_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.should_be_add_basket_link()
        page.go_to_good_page()          #
        page.should_be_same_good_name()
        page.should_be_same_good_prices()

        page.should_not_be_dissapeared_success_message()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_good_page()
        page.should_be_same_good_name()
        page.should_be_same_good_prices()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_link()
        basketPage = BasketPage(browser, browser.current_url)
        basketPage.should_be_empty_basket()
        print(1)

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        