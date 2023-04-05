import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
try:
    #username:password@
    # URL="https://the-internet.herokuapp.com/basic_auth"
    URL="https://admin:admin@the-internet.herokuapp.com/basic_auth"
    driver.get(URL)
    message=driver.find_element(By.CSS_SELECTOR,"p").text
    print(message) #Congratulations! You must have the proper credentials.
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/")
    driver.implicitly_wait(5)
    driver.find_element(By.LINK_TEXT,"File Upload").click()
    choose_file=driver.find_element(By.ID, "file-upload") #.click()
    choose_file.send_keys(r"C:\Users\dineshkumar.singaram\PycharmProjects\CheckOut\Selenium-Python\DUmmy.txt")
    driver.find_element(By.CSS_SELECTOR, "input[value=Upload]").click()
    print("File Uploaded! successfully")
except Exception as e:
    print("username and password not entered")