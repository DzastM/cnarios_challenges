from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from features.pages.base_page import BasePage

class ProductPurchasingPage(BasePage):
    HEADING = (By.TAG_NAME, "h1")
    URL = "https://www.cnarios.com/challenges/product-purchasing"
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "header button")
    CART_SELECTOR = (By.CSS_SELECTOR, ".space-y-4 > div")
    PRODUCT_NAME = (By.XPATH, ".//p[contains(.,'($')]")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".space-x-2 > p")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".font-semibold")
    TOTAL_PRICE = (By.XPATH, ".//h6[contains(text(),'Total:')]")

    def get_heading_text(self):
        return self.driver.find_element(*self.HEADING).text
    
    def add_product_to_cart(self, product_name):
        product_locator = By.XPATH, f"//div[h6='{product_name}']//div[button]"
        self.move_to_element(product_locator)
        self.click_element(product_locator)

    def click_view_cart(self):
        self.scroll_to_top()
        self.click_element(self.VIEW_CART_BUTTON)

    def get_cart_items(self) -> dict:
        cart_items_selector = self.driver.find_elements(*self.CART_SELECTOR)
        full_cart_items_info = {}  # Dictionary of items in format {item_name: (quantity, price)}
        for item in cart_items_selector:
            full_cart_items_info[item.find_element(*self.PRODUCT_NAME).text.split('(')[0].strip()] = (item.find_element(*self.PRODUCT_QUANTITY).text, item.find_element(*self.PRODUCT_PRICE).text)
        return full_cart_items_info       
    
    def get_item_name_and_quantity(self) -> dict:
        item_names_and_quantities = {}
        full_cart_items_info = self.get_cart_items()
        for item_name in full_cart_items_info:
            item_names_and_quantities[item_name] = int(full_cart_items_info[item_name][0])  # Extracting quantity from the tuple
        return item_names_and_quantities

    def get_total_price(self) -> str:
        return self.driver.find_element(*self.TOTAL_PRICE).text.split(':')[1].strip()