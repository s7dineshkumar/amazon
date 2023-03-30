from selenium.webdriver.common.by import By

class ProductDetailsPage():
    def __init__(self,driver):
        self.driver=driver

    addtocartbutton=(By.ID,"add-to-cart-button")
    addedtocartmessage=(By.XPATH, "//span[contains(text(),'Added to Cart')]")
    gotocartbutton=(By.XPATH,"//div[@id='sw-atc-buy-box']//a[contains(text(),'Go to Cart')]")
    skip1=(By.CSS_SELECTOR, "span#attachSiNoCoverage-announce")

    def addtoCart(self):
        return self.driver.find_element(*ProductDetailsPage.addtocartbutton)

    def addedtoCart(self):
        return self.driver.find_element(*ProductDetailsPage.addedtocartmessage).text

    def skipProtect(self):
        return self.driver.find_element(*ProductDetailsPage.skip1)

    def gotoCart(self):
        return self.driver.find_element(*ProductDetailsPage.gotocartbutton)

