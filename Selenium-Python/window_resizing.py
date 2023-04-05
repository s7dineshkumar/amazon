import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
try:
    #username:password@
    URL="https://admin:admin@the-internet.herokuapp.com/basic_auth"
    driver.get(URL)
    message=driver.find_element(By.CSS_SELECTOR,"p").text
    print(message) #Congratulations! You must have the proper credentials.
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/")
    driver.set_window_size(600,700)
    driver.set_window_position(150,150)
    driver.find_element(By.LINK_TEXT,"File Upload").click()
except Exception as e:
    print("username and password not entered")