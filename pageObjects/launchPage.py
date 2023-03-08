# common actions in Homepage
import pytest
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self,driver): # constructor
        # super().__init__(driver)
        self.driver=driver

    #variables: element of the common actions
    searchbox= (By.CSS_SELECTOR, "input[aria-label='Search Amazon.in']")
    searchbutton=(By.ID,"nav-search-submit-button")

    def clickSearchTextBox(self):
        return self.driver.find_element(*HomePage.searchbox)
        #home=HomePage() - object
    def enterSearchText(self,searchBoxText):
        searchboxclick = self.clickSearchTextBox()
        searchboxclick.click()
        searchboxclick.clear()
        searchboxclick.send_keys(searchBoxText)
    def clickSearch(self):
        self.driver.find_element(*HomePage.searchbutton).click()

