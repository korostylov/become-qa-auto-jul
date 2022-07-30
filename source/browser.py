import pytest
from read_config import config

from selenium.webdriver import Chrome

class Browser():

    @pytest.fixture
    def browser():
    # Initialize ChromeDriver
        if config['browser'] == 'chrome':
            driver = Chrome
        else:
            raise Exception(f'"{config["browser"]}" is not a supported browser')

        # Wait implicitly for elements to be ready before attempting interactions
        driver.implicitly_wait(config['wait_time'])
        
        # 
        driver.maximize_window
        
        # Return the driver object at the end of setup
        yield driver
        
        # For cleanup, quit the driver
        driver.quit()

