import fixture as fixture
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class", autouse=True)
def setup(request):
    driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
