from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login_form button.btn')

    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form button.btn')