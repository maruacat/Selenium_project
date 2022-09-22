from .pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage
from .pages.base_page import BasePage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_form()
    login_page.should_be_register_form()
    login_page.should_be_login_url()

    

