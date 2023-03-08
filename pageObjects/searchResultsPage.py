import pytest
from selenium.webdriver.common.by import By

class ResultsPage:
    def __init__(self,driver):
        # super().__init__(driver)
        self.driver=driver

    resultTitle=(By.CSS_SELECTOR, "span[aria-label='Current page, page 1']")

    def getTitle(self):
        self.driver.find_element(*self.resultTitle)
    def screenshot(self,filename):
        self.driver.get_screenshot_as_file(filename)
