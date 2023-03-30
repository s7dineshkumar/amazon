from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self,driver):
        self.driver=driver

    cartpagetext=(By.XPATH,"//span[@class='a-truncate-cut' and contains(text(),'Apple 20W USB-C Power Adapter (for iPhone, iPad & AirPods)')]")
    shoppingcart=(By.XPATH, "//div[@data-name='Active Cart']//h1[contains(text(),'Shopping Cart')]")

    def shoppingCart(self):
        return self.driver.find_element(*CartPage.shoppingcart).text

    def cartPageTitle(self):
        return self.driver.find_element(*CartPage.cartpagetext).text