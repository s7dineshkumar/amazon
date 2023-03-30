import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)
        fileHandler=logging.FileHandler('logfile.log')
        formatter=logging.Formatter("%(asctime)s: %(levelname)s: %(filename)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def elementToBeClickable(self,locator):
        wait=WebDriverWait(self.driver,10)
        element_click=wait.until(EC.element_to_be_clickable(locator))
        return element_click

    def allElementsLoaded(self,locator):
        wait = WebDriverWait(self.driver,10)
        allElements = wait.until(EC.presence_of_all_elements_located(locator))
        return allElements

    def presenceofelement(self,locator):
        wait = WebDriverWait(self.driver,10)
        element_presence = wait.until(EC.presence_of_element_located(locator))
        return element_presence

    def switchWindow(self):
        window=self.driver.window_handles
        newtab=self.driver.switch_to.window(window[1])
        return newtab

