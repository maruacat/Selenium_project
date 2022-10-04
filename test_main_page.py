from Selenium_project.pages.basket_page import BasketPage
from .pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser,link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)   #инициализируем страницу Корзина
    basket_page.product_should_not_be_in_basket()
    basket_page.text_your_basket_is_empty_present()



