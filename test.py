import time
from webdriver_set import driver_setup
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from contact import contact_us_message_valid
from about import about_us

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.my_driver = driver_setup()
        self.my_driver.get('https://thedemosite.co.uk/contact/')

    def test1(self):
        contact_us_message_valid(self.my_driver)
        time.sleep(0.5)
        element = self.my_driver.find_element(By.CLASS_NAME, 'uagb-forms-success-message-173d6c98')
        assert not element.is_displayed()

    def test2(self):
        about_us(self.my_driver)
        time.sleep(0.5)


    def tearDown(self) -> None:
        self.my_driver.close()