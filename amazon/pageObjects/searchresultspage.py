from selenium.webdriver.common.by import By

class SearchResultsPage():
    def __init__(self,driver):
        self.driver=driver

    brandapple=(By.XPATH,"//span[text()='Apple']")
    appleusb=(By.XPATH,"//span[@data-component-type='s-search-results']//span[text()='Apple 20W USB-C Power Adapter (for iPhone, iPad & AirPods)']")

    def brand(self):
        self.driver.find_element(*SearchResultsPage.brandapple).click()

    def appleUSBtitle(self):
        titleinsearchresult=self.driver.find_element(*SearchResultsPage.appleusb).text
        return titleinsearchresult

    def appleUSBclick(self):
        self.driver.find_element(*SearchResultsPage.appleusb).click()
