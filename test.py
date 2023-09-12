import time
from webdriver_set import driver_setup
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from contact import contact_us_message_valid

from privacy_policy import privacy_policy

from about import about_us

from Logo_page import logo_page

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = driver_setup()
        self.driver.get('https://thedemosite.co.uk/contact/')

    def test1(self):
        contact_us_message_valid(self.driver)
        time.sleep(0.5)
        element = self.driver.find_element(By.CLASS_NAME, 'uagb-forms-success-message-173d6c98')
        assert not element.is_displayed()


    def test3(self):
        privacy_policy(self.driver)
    def test2(self):
        about_us(self.driver)

        time.sleep(0.5)

    def test4(self):
        logo_page(self.driver)
        time.sleep(0.5)

    def tearDown(self) -> None:
        self.driver.close()


