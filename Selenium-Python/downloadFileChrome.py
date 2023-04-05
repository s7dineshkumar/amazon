import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\dineshkumar.singaram\PycharmProjects\CheckOut\report"})
  # "download.prompt_for_download": False,
  # "download.directory_upgrade": True,
  # "safebrowsing.enabled": True})
driver=webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
try:
    driver.get("https://www.selenium.dev/downloads/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//a[@href='https://pypi.python.org/pypi/selenium']").click()
    driver.find_element(By.CSS_SELECTOR, "a[href='/project/selenium/'] span").click()
except Exception as e:
    print("username and password not entered")