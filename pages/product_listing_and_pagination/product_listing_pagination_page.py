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
    PRODUCTS = "//div[contains(@class,'grid') and contains(@class,'w-full')]/*"
    PRODUCT_NAME = ".//h6[contains(@class,'font-semibold')]"
    PRODUCT_CATEGORY = ".//p"
    PRODUCT_PRICE = ".//h6[contains(text(),'$')]"
    PRODUCT_RATING = ".//span[contains(@class,'MuiRating-root')]"  # Get 'aria-label'attribute for rating value in format "X Stars"
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