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