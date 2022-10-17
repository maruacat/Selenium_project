from Selenium_project.pages.basket_page import BasketPage
from Selenium_project.pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from .pages.base_page import BasePage
from .pages.product_page import ProductPage




link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

# def test_guest_can_add_product_to_busket(browser):
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_product_to_basket()
#     product_page.should_be_same_name()
#     product_page.should_be_same_price()

# def test_guest_should_see_login_link_on_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser): 
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#     page.go_to_login_page()

# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     page = BasePage(browser, link)
#     page.open()
#     page.go_to_basket()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.product_should_not_be_in_basket()
#     basket_page.text_your_basket_is_empty_present

class TestLoginFromProductPage():
        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
            email = str(time.time()) + "@fakemail.org"
            password = 'test12345678'
            product_page = ProductPage(browser, link)
            product_page.open()
            product_page.go_to_login_page()
            login_page = LoginPage(browser, browser.current_url)
            login_page.register_new_user(email,password)
            base_page = BasePage(browser, browser.current_url)
            base_page.should_be_authorized_user()
            

        def test_user_cant_see_success_message_after_adding_product_to_basket(self,browser):
            product_page = ProductPage(browser, link)
            product_page.open()
            product_page.add_product_to_basket()
            product_page.should_not_be_success_message()
            
        

        def test_user_can_add_product_to_busket(self,browser):
            product_page = ProductPage(browser, link)
            product_page.open()
            product_page.add_product_to_basket()
            product_page.should_be_same_name()
            product_page.should_be_same_price()