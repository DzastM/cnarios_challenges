from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage
from features.pages.product_purchasing import ProductPurchasingPage

class ChallengesPage(BasePage):
    HEADING = (By.TAG_NAME, "h1")
    PRODUCT_LISTING_PAGINATION_TEXT = "E-commerce Product Listing & Pagination"
    PRODUCT_FILTERING_SEARCH_TEXT = "E-commerce Product Filtering & Search"
    ROLE_BASED_LOGIN_FLOW_TEXT = "Role-Based Login Flow"
    PRODUCT_PURCHASING_TEXT = "E-commerce End-to-End Product Purchasing Flow"
    SOCIAL_MEDIA_FEED_TEXT = "Social Media Feed Interaction Challenge"
    SHADOW_DOM_LOGIN_FORM_TEXT = "Shadow DOM Login Form Interaction Challenge"
    SIMPLE_SEARCH_ENGINE_TEXT = "Simple Search Engine UI Automation Challenge"
    JOB_APPLICATION_FORM_TEXT = "Job Application Form Automation Challenge"
    VIEW_PRODUCT_PURCHASING_CHALLENGE_BUTTON = (By.XPATH, f"//h2[contains(., '{PRODUCT_PURCHASING_TEXT}')]/../..//button[contains(., 'View Challenge')]")


    def get_heading_text(self):
        return self.driver.find_element(*self.HEADING).text
    
    def clickChallengeButton(self, name:str) -> None:
        if name == self.PRODUCT_PURCHASING_TEXT:
            self.clickButton(self.VIEW_PRODUCT_PURCHASING_CHALLENGE_BUTTON)
            return ProductPurchasingPage(self.driver)
        
    