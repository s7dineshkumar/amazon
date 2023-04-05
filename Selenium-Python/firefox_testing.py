from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# options = Options()
# opt_bin=options.binary_location=r'C:\Program Files\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(executable_path=r"C:\Users\dineshkumar.singaram\PycharmProjects\CheckOut\geckodriver.exe", options=opt_bin)
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.yatra.com/")
# try:
#     driver.find_element(By.CSS_SELECTOR, "a[title='Round Trip']").click()
# except Exception as e:
#     print("Test case is not executed")

try:
    id=driver.find_elements(By.XPATH, "//*[@class]")

    for value in id:
        print(value.get_attribute('class'))
except Exception as e:
    print('Test failed')

