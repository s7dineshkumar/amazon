# baseclass will have all the methods related to the requirement
# common methods: element clicks, element presence, radio button, drop down
import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyElementIsClickable(self,locator):
        wait=WebDriverWait(self.driver, 10)
        element_clickable=wait.until(EC.element_to_be_clickable(locator))
        return element_clickable

    def verifyAllElementsPresence(self, locator):
        wait=WebDriverWait(self.driver, 10)
        all_elements_presence=wait.until(EC.presence_of_all_elements_located(locator))
        return all_elements_presence

    def verifyLinkPresence(self, locator):
        wait=WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, locator)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)