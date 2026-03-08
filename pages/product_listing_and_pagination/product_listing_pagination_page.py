from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from ..base_page import BasePage

class ProductListingPaginationPage(BasePage):

    HEADER = (By.TAG_NAME, "h1")
    EXPECTED_HEADER_TEXT = "E-commerce Product Listing & Pagination"
    URL = "https://www.cnarios.com/challenges/product-listing-pagination"
    NEXT_BUTTON = "//button[text()='Next']"
    PREVIOUS_BUTTON = "//button[text()='Prev']"
    PAGINATION_LEFT_ARROW = "//button[@aria-label='Go to previous page']"
    PAGINATION_RIGHT_ARROW = "//button[@aria-label='Go to next page']"
    PAGINATION_CURRENT_PAGE = "//button[@aria-current='page']"
    PRODUCTS = "//div[contains(@class,'grid') and contains(@class,'w-full')]/*"
    PRODUCT_NAME = ".//h6[contains(@class,'font-semibold')]"
    PRODUCT_CATEGORY = ".//p"
    PRODUCT_PRICE = ".//h6[contains(text(),'$')]"
    PRODUCT_RATING = ".//span[contains(@class,'MuiRating-root')]"  # Get 'aria-label' attribute for rating value in format "X Stars"
    CATEGORIES = {
        "Books": 0,
        "Electronics": 0,
        "Home": 0,
        "Clothing": 0,
        "Sports": 0
    }
    CATEGORIES_LISTED = "//h2['Categories']/following-sibling::div[contains(@class,'grid')]/*"
    CATEGORIES_NAMES = ".//p[contains(@class,'uppercase')]"
    CATEGORIES_COUNTS = ".//p[contains(@class,'font-bold')]"

    def click_next_page(self):
        next_button = self.driver.find_element(By.XPATH, self.NEXT_BUTTON)
        if next_button.is_enabled():
            next_button.click()

    def click_previous_page(self):
        previous_button = self.driver.find_element(By.XPATH, self.PREVIOUS_BUTTON)
        if previous_button.is_enabled():
            previous_button.click()

    def count_products_in_category(self, category):
        products = self.driver.find_elements(By.XPATH, self.PRODUCTS)
        for product in products:
            product_category = product.find_element(By.XPATH, self.PRODUCT_CATEGORY).text.rsplit(' ', 1)[-1]  # Extract category from text like "Category: Books"
            self.CATEGORIES[category] += 1
            self.store_data(category, self.CATEGORIES[category])  # Store the count for later verification
        self.click_next_page()

    def count_products_in_each_category(self):
        for category in self.CATEGORIES.keys():
            self.count_products_in_category(category)

    def get_category_counts(self, category):
        return self.get_data(category)

    def verify_product_counts(self):
        categories_counts = self.driver.find_elements(By.XPATH, self.CATEGORIES_LISTED)
        for category in categories_counts:
            category_name = category.find_element(By.XPATH, self.CATEGORIES_NAMES).text.capitalize()  # Extract category name and capitalize to match keys in self.CATEGORIES
            expected_count = int(category.find_element(By.XPATH, self.CATEGORIES_COUNTS).text.strip('()'))            
            actual_count = self.get_category_counts(category_name)
            assert expected_count == actual_count, f"Expected {expected_count} products in category '{category_name}', but found {actual_count}."
    
    def search_product_by_name(self, product_name):
        while self.driver.find_element(By.XPATH, self.NEXT_BUTTON).get_attribute("disabled") is None:  # While the "Next" button is enabled
            products = self.driver.find_elements(By.XPATH, self.PRODUCTS)
            for product in products:
                current_product_name = product.find_element(By.XPATH, self.PRODUCT_NAME).text
                if current_product_name.lower() == product_name.lower():
                    return product  # Return the WebElement of the found product
            self.click_next_page()
        raise Exception(f"Product with name '{product_name}' not found.")

    
    def verify_product_data(self, product_name, price, category, stars):
        product = self.search_product_by_name(product_name)
        actual_price = product.find_element(By.XPATH, self.PRODUCT_PRICE).text
        actual_category = product.find_element(By.XPATH, self.PRODUCT_CATEGORY).text.rsplit(' ', 1)[-1]  # Extract category from text like "Category: Books"
        actual_stars = product.find_element(By.XPATH, self.PRODUCT_RATING).get_attribute("aria-label").split()[0]  # Get the number of stars from 'aria-label' attribute
        assert actual_price == price, f"Expected price '{price}' for product '{product_name}', but found '{actual_price}'."
        assert actual_category == category, f"Expected category '{category}' for product '{product_name}', but found '{actual_category}'."
        assert actual_stars == stars, f"Expected {stars} stars for product '{product_name}', but found {actual_stars}."

    def get_current_page_number(self):
        pagination_info = self.driver.find_element(By.XPATH, self.PAGINATION_CURRENT_PAGE).text
        current_page = int(pagination_info)
        return current_page
    
    def assert_page_number(self, expected_page_number):
        current_page = self.get_current_page_number()
        assert current_page == expected_page_number, f"Expected to be on page {expected_page_number}, but currently is on page {current_page}."