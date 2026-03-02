from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage

class ProductPurchasingPage(BasePage):
    HEADING = (By.TAG_NAME, "h1")
    URL = "https://www.cnarios.com/challenges/product-purchasing"
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "header button")

    

    def get_heading_text(self):
        return self.driver.find_element(*self.HEADING).text
    
    def add_product_to_cart(self, product_name):
        product_locator = (By.XPATH, f"//div[h6='{product_name}']//div[button]")
        self.driver.find_element(*product_locator).click()
        self.driver.implicitly_wait(2)  # Wait for the cart to update

    def click_view_cart(self):
        cart_button = self.driver.find_element(*self.VIEW_CART_BUTTON)
        cart_button.click()

    def get_cart_items(self) -> list:
        cart_items = self.driver.find_elements(By.CSS_SELECTOR, ".space-y-4 > div")
        list_of_items = {}
        for item in cart_items:
            list_of_items[item.find_element(By.XPATH, "//p[contains(.,'($')]").text] = (item.find_element(By.CSS_SELECTOR, ".space-x-2 > p").text, item.find_element(By.CSS_SELECTOR, ".font-semibold").text)
            
        print(list_of_items)
        return list_of_items
        
        