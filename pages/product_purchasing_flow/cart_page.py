from selenium.webdriver.common.by import By

from ..base_page import BasePage
import pages.product_purchasing_flow.product_purchasing_page

class CartPage(BasePage):

    CART_SELECTOR = (By.CSS_SELECTOR, ".space-y-4 > div")
    PRODUCT_NAME = (By.XPATH, ".//p[contains(.,'($')]")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".space-x-2 > p")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".font-semibold")
    TOTAL_PRICE = (By.XPATH, ".//h6[contains(text(),'Total:')]")
    PROCEED_TO_ADRESS_BUTTON = (By.XPATH, "//button[contains(., 'Proceed to Address')]")
    PROCEED_TO_PAYMENT_BUTTON = (By.XPATH, "//button[contains(., 'Proceed to Payment')]")
    FIRST_NAME_INPUT = (By.XPATH, "//div[label='First Name']//input")
    LAST_NAME_INPUT = (By.XPATH, "//div[label='Last Name']//input")
    ADDRESS_INPUT = (By.XPATH, "//div[label='Address']//textarea[1]")
    PAY_NOW_BUTTON = (By.XPATH, "//button[contains(., 'Pay Now')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(., 'Cancel')]")
    BILLING_DETAILS_FIRST_AND_LAST_NAME = (By.XPATH, "//div[h6='Billing Details:']//p[1]")
    BILLING_DETAILS_ADDRESS = (By.XPATH, "//div[h6='Billing Details:']//p[2]")
    ORDER_PLACED_SUCCESSFULLY_MESSAGE = (By.XPATH, "//h5[contains(text(),'Order Placed Successfully!')]")
    BACK_TO_HOME_BUTTON = (By.XPATH, "//button[contains(., 'Back to Home')]")
    PAYMENT_FAILED_MESSAGE = (By.XPATH, "//h6[contains(.,'Payment Failed')]")

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

    def update_product_quantity(self, product_name:str, expected_quantity:int):
        current_quantity = int(self.get_item_name_and_quantity()[product_name])
        minus_button = (By.XPATH, f"//p[contains(normalize-space(.),'{product_name}')]/following-sibling::div//button[1]")
        plus_button = (By.XPATH, f"//p[contains(normalize-space(.),'{product_name}')]/following-sibling::div//button[2]")

        if current_quantity < expected_quantity:
            for _ in range(expected_quantity - current_quantity):

                self.click_element(plus_button)
        elif current_quantity > expected_quantity:
            for _ in range(current_quantity - expected_quantity):
                self.click_element(minus_button)

    def assert_if_cart_is_empty(self):
            actual_items_list = self.get_item_name_and_quantity()
            assert len(actual_items_list) == 0, f"Expected cart to be empty, but found items: {actual_items_list}"

    def assert_total_price(self, expected_total_price:str):
           actual_total_price = self.get_total_price()
           assert actual_total_price == expected_total_price, f"Expected total price '{expected_total_price}', but got '{actual_total_price}'"

    def click_proceed_to_address(self):
        self.click_element(self.PROCEED_TO_ADRESS_BUTTON)
    
    def click_proceed_to_payment(self):
        self.click_element(self.PROCEED_TO_PAYMENT_BUTTON)

    def assert_proceed_to_payment_button_disabled(self):
        button = self.driver.find_element(*self.PROCEED_TO_PAYMENT_BUTTON)
        assert not button.is_enabled(), "Expected 'Proceed to Payment' button to be disabled, but it is enabled"

    def fill_in_address_form(self, first_name:str, last_name:str, address:str):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.store_data('First Name', first_name)
        self.store_data('Last Name', last_name)
        self.store_data('Address', address)
    
    def click_pay_now(self):
        self.click_element(self.PAY_NOW_BUTTON)
    
    def click_cancel(self):
        self.click_element(self.CANCEL_BUTTON)
    
    def verify_billing_user_details(self):
        expected_first_name = self.get_data('First Name')
        expected_last_name = self.get_data('Last Name')
        expected_address = self.get_data('Address')

        actual_first_name = self.driver.find_element(*self.BILLING_DETAILS_FIRST_AND_LAST_NAME).text.split()[0]
        actual_last_name = self.driver.find_element(*self.BILLING_DETAILS_FIRST_AND_LAST_NAME).text.split()[1]
        actual_address = self.driver.find_element(*self.BILLING_DETAILS_ADDRESS).text
        
        assert expected_first_name == actual_first_name, f"Expected first name '{expected_first_name}', but got '{actual_first_name}'"
        assert expected_last_name == actual_last_name, f"Expected last name '{expected_last_name}', but got '{actual_last_name}'"
        assert expected_address == actual_address, f"Expected address '{expected_address}', but got '{actual_address}'"

    def verify_order_successfully_placed(self):
        success_message = self.driver.find_element(*self.ORDER_PLACED_SUCCESSFULLY_MESSAGE)
        assert success_message.is_displayed(), "Expected 'Order Placed Successfully!' message to be displayed, but it is not"

    def click_go_home_button(self):
        self.click_element(self.BACK_TO_HOME_BUTTON)
        return pages.product_purchasing_flow.product_purchasing_page.ProductPurchasingPage(self.driver)

    def assert_go_home_button_is_displayed(self):
        go_home_button = self.driver.find_element(*self.BACK_TO_HOME_BUTTON)
        assert go_home_button.is_displayed(), "Expected 'Go Home' button to be displayed, but it is not"

    def assert_payment_failed_message_displayed(self):
        payment_failed_message = self.driver.find_element(*self.PAYMENT_FAILED_MESSAGE)
        assert payment_failed_message.is_displayed(), "Expected 'Payment Failed' message to be displayed, but it is not"