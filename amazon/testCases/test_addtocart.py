import time

from selenium.webdriver.common.by import By

from amazon.Utils.baseclass import BaseClass
from amazon.Utils.utilities import Utils
from amazon.pageObjects.cartpage import CartPage
from amazon.pageObjects.detailspage import ProductDetailsPage
from amazon.pageObjects.homepage import HomePage
from amazon.pageObjects.searchresultspage import SearchResultsPage

class Test_AddToCart(BaseClass):
    # skip = (By.XPATH, "//span[@id='attachSiNoCoverage']//span[contains(text(),' Skip ')]")
    skip1=(By.CSS_SELECTOR, "span#attachSiNoCoverage-announce")
    addedtocartmessage = (By.XPATH, "//span[contains(text(),'Added to Cart')]")

    def test_addToCart(self):
        log=self.getLogger()
        homePage=HomePage(self.driver)
        mobilem=homePage.subMenu()
        mobilem.click()
        searchResultsPage=SearchResultsPage(self.driver)
        searchResultsPage.brand()
        titleinsearchresults=searchResultsPage.appleUSBtitle()
        log.info("Search results page title is captured")
        searchResultsPage.appleUSBclick()
        self.switchWindow()
        detailsPage=ProductDetailsPage(self.driver)
        addcart=detailsPage.addtoCart()
        addcart.click()
        skippro=self.presenceofelement(self.skip1)
        skippro.click()
        # afteradd = self.presenceofelement(self.addedtocartmessage)
        # print(afteradd.text)
        print(detailsPage.addedtoCart())
        log.info("product is added to cart")
        detailsPage.gotoCart().click()
        cartPage=CartPage(self.driver)
        print(cartPage.shoppingCart())
        titleincart=cartPage.cartPageTitle()
        log.info("cart page title is captured")
        assert titleinsearchresults == titleincart