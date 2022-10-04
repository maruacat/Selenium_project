from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def product_should_not_be_in_basket (self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET)
    def text_your_basket_is_empty_present(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_YOUR_BASKET_IS_EMPTY), "Text your basket is empty not present"
        control_text = "Your basket is empty"
        message_your_basket_is_empty = self.browser.find_element(*BasketPageLocators.TEXT_YOUR_BASKET_IS_EMPTY).text
        assert control_text in message_your_basket_is_empty, "No your basket is empty message"