from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from ..base_page import BasePage
import random

class ProductFilteringAndSearchPage(BasePage):

    HEADER = (By.TAG_NAME, "h1")
    EXPECTED_HEADER_TEXT = "E-commerce Product Filtering & Search"
    URL = "https://www.cnarios.com/challenges/product-filtering"
    CATEGORY_FILTER_DROPDOWN = (By.CSS_SELECTOR, "div[role='combobox'][aria-labelledby='category']")
    PRODUCTS = "//h6[text()='Products']/following-sibling::div"
    PRODUCT_NAME = ".//p[1]"
    PRODUCT_CATEGORY_AND_PRICE = ".//p[2]"
    PRODUCT_STOCK_STATUS = ".//span"

    def filter_by_category(self, category):
        dropdown = self.driver.find_element(*self.CATEGORY_FILTER_DROPDOWN)
        dropdown.click()
        option = self.driver.find_element(By.CSS_SELECTOR, f"*[role='option'][data-value='{category}']")
        option.click()

    def verify_product_category(self, expected_category):
        products = self.driver.find_elements(By.XPATH, self.PRODUCTS)
        for product in products:
            product_category = product.find_element(By.XPATH, self.PRODUCT_CATEGORY_AND_PRICE).text.split()[0]
            assert product_category == expected_category, f"Expected category '{expected_category}', but found '{product_category}'"















    def click_next_page(self):
        next_button = self.driver.find_element(By.XPATH, self.NEXT_BUTTON)
        if next_button.is_enabled():
            next_button.click()

    def click_previous_page(self):
        previous_button = self.driver.find_element(By.XPATH, self.PREVIOUS_BUTTON)
        if previous_button.is_enabled():
            previous_button.click()

    def click_page(self, page_number):
        page_button = self.driver.find_element(By.XPATH, f"//button[@aria-label='Go to page {page_number}']")
        if page_button.is_enabled():
            page_button.click()

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

    def reset_category_counts(self):
        self.CATEGORIES = dict.fromkeys(self.CATEGORIES, 0)  # Reset any stored values

    def verify_product_counts(self):        
        categories_counts = self.driver.find_elements(By.XPATH, self.CATEGORIES_LISTED)
        for category in categories_counts:
            category_name = category.find_element(By.XPATH, self.CATEGORIES_NAMES).text.capitalize()  # Extract category name and capitalize to match keys in self.CATEGORIES
            expected_count = int(category.find_element(By.XPATH, self.CATEGORIES_COUNTS).text.strip('()'))            
            actual_count = self.get_category_counts(category_name)
            assert expected_count == actual_count, f"Expected {expected_count} products in category '{category_name}', but found {actual_count}."
        self.reset_category_counts()  # Reset counts after verification

    def search_product_by_name(self, product_name):
        while True:
            products = self.driver.find_elements(By.XPATH, self.PRODUCTS)
            for product in products:
                current_product_name = product.find_element(By.XPATH, self.PRODUCT_NAME).text
                if current_product_name.lower() == product_name.lower():
                    return product  # Return the WebElement of the found product
            if self.driver.find_element(By.XPATH, self.NEXT_BUTTON).get_attribute("disabled") is None:  # While the "Next" button is enabled
                self.click_next_page()
            else:
                break
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

    def find_products_by_rating(self, expected_rank):
        while True:
            products = self.driver.find_elements(By.XPATH, self.PRODUCTS)
            for product in products:
                current_rating = product.find_element(By.XPATH, self.PRODUCT_RATING).get_attribute("aria-label").split()[0]  # Get the number of stars from 'aria-label' attribute
                if int(current_rating) == expected_rank:
                    product_name = product.find_element(By.XPATH, self.PRODUCT_NAME).text
                    product_category = product.find_element(By.XPATH, self.PRODUCT_CATEGORY).text.rsplit(' ', 1)[-1]  # Extract category from text like "Category: Books"
                    self.store_data(product_name, product_category)
            if self.driver.find_element(By.XPATH, self.NEXT_BUTTON).get_attribute("disabled") is None:  # While the "Next" button is enabled
                self.click_next_page()
            else:
                break
    
    def assert_product_has_rating(self, product_name, rating):
        assert(product_name in self.data_store), f"Expected to find product '{product_name}' with rating {rating}, but it was not found."

    def find_most_expensive_products_in_each_category(self):
        most_expensive_products = {
            "Books": {"name": None, "price": "0"},
            "Electronics": {"name": None, "price": "0"},
            "Home": {"name": None, "price": "0"},
            "Clothing": {"name": None, "price": "0"},
            "Sports": {"name": None, "price": "0"}
        }
        while True:
            products = self.driver.find_elements(By.XPATH, self.PRODUCTS)
            for product in products:
                product_price = product.find_element(By.XPATH, self.PRODUCT_PRICE).text
                product_category = product.find_element(By.XPATH, self.PRODUCT_CATEGORY).text.rsplit(' ', 1)[-1]
                current_highest_price = most_expensive_products[product_category]['price']
                if float(product_price.strip('$')) > float(current_highest_price.strip('$')):
                    product_name = product.find_element(By.XPATH, self.PRODUCT_NAME).text
                    most_expensive_products[product_category]['name'] = product_name
                    most_expensive_products[product_category]['price'] = product_price
            if self.driver.find_element(By.XPATH, self.NEXT_BUTTON).get_attribute("disabled") is None:  # While the "Next" button is enabled
                self.click_next_page()
            else:
                break
        self.store_data("most_expensive_products", most_expensive_products)

    def assert_most_expensive_product(self, category, product_name):
        most_expensive_products = self.get_data("most_expensive_products")
        expected_product_name = most_expensive_products[category]["name"]
        assert expected_product_name == product_name, f"Expected most expensive product in category '{category}' to be '{product_name}', but found '{expected_product_name}'."

    def navigate_to_page(self, page_number):
        while True:
            current_page = self.get_current_page_number()
            if current_page < page_number:
                if self.driver.find_element(By.XPATH, self.PAGINATION_RIGHT_ARROW).get_attribute("disabled") is None:  # While the right arrow is enabled
                    self.click_next_page()
                else:
                    break
            elif current_page > page_number:
                if self.driver.find_element(By.XPATH, self.PAGINATION_LEFT_ARROW).get_attribute("disabled") is None:  # While the left arrow is enabled
                    self.click_previous_page()
                else:
                    break
            else:
                break
    
    def get_total_pages(self):
        last_page = self.driver.find_element(By.CSS_SELECTOR, "nav ul li:nth-last-child(2) button").get_attribute("aria-label").split()[-1]
        return int(last_page)

    def verify_product_card_format(self):
        products = self.driver.find_elements(By.XPATH, self.PRODUCTS)
        for product in products:
            assert product.find_element(By.XPATH, self.PRODUCT_NAME).is_displayed(), "Product name is not displayed on the product card."
            assert product.find_element(By.XPATH, self.PRODUCT_PRICE).is_displayed(), "Product price is not displayed on the product card."
            assert product.find_element(By.XPATH, self.PRODUCT_CATEGORY).is_displayed(), "Product category is not displayed on the product card."
            assert product.find_element(By.XPATH, self.PRODUCT_RATING).is_displayed(), "Product star rating is not displayed on the product card."
    
    def verify_rating_stars(self):
        assert self.driver.find_elements(By.XPATH, f"({self.PRODUCT_RATING})[{random.randint(1,10)}]"), "Rating stars are not visible on the product cards."