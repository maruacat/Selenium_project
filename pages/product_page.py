from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasePageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_busket_button = self.browser.find_element(*ProductPageLocators.ADD_IN_BUSKET)
        add_busket_button.click()
    def should_be_same_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME)
        assert product_name.text == message_product_name.text, 'Product name not same'

    
    def should_be_same_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        message_product_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE)
        assert product_price.text == message_product_price.text, 'Product price not eql'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    
        





