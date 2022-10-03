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

class ProductPageLocators():
    ADD_IN_BUSKET = (By.CSS_SELECTOR, 'form#add_to_basket_form button.btn')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, 'div#messages div.alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main p')
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.alertinner p strong')
