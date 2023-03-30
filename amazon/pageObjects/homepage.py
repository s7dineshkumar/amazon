from selenium.webdriver.common.by import By

class HomePage():
    def __init__(self,driver):
        self.driver=driver

    mobiles=(By.XPATH,"//div[@id='nav-xshop-container']//a[contains(text(),'Mobiles')]")

    def subMenu(self):
        return self.driver.find_element(*HomePage.mobiles)