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
except Exception as e:
    print("ERROR: Test Case Failed")