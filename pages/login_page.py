from Selenium_project.conftest import browser
from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# email = str(time.time()) + "@fakemail.org"
# password = 'test123'

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'Url is not include login'

    def should_be_login_form(self):
         assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present'
       
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not present'


    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        email_field_register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_field_register_form.send_keys(email)
        password_field_register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        password_field_register_form.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD)
        confirm_password_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
    



