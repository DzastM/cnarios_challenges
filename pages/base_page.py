from selenium.webdriver.common.action_chains import ActionChains
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def click_element(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def move_to_element(self, by_locator):
        element = self.driver.find_element(*by_locator)
        ActionChains(self.driver).move_to_element(element).perform()
    
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def store_data(self, key, value):
        if not hasattr(self, 'data_store'):
            self.data_store = {}
        self.data_store[key] = value

    def get_data(self, key):
        return self.data_store.get(key, None)

    def assert_header(self, expected_header):
        actual_header = self.driver.find_element(*self.HEADER).text
        assert actual_header == expected_header, f"Expected header to be '{expected_header}', but got '{actual_header}'"

    def clear_local_storage(self):
        self.driver.execute_script("window.localStorage.clear();")