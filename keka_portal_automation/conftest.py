import pytest
from selenium import webdriver

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
 # optional, if you want to manage drivers automatically
from webdriver_manager.chrome import ChromeDriverManager 

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Set up Chrome options (e.g., headless mode)
    options = webdriver.ChromeOptions()
    
    # Optional: Uncomment the next line if you want to run in headless mode
    # options.add_argument("--headless")
    
    # Automatically download and manage the ChromeDriver
    driver_path = ChromeDriverManager().install()

    # Create Chrome WebDriver instance with the managed driver
    # driver = webdriver.Chrome(service=Service(driver_path), options=options)
    
    yield driver  # Yield the driver to the test
    
    driver.quit()  # Quit the driver after the test is finished
 


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


def pytest_addoption(parser):
    parser.addoption("--browser")
