import time
from webdriver_set import driver_setup
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from contact import contact_us_message_valid
<<<<<<< HEAD
from privacy_policy import privacy_policy

=======
from about import about_us
>>>>>>> 4e13ada5436d841bc8acf779810c024b8879853c

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = driver_setup()
        self.driver.get('https://thedemosite.co.uk/contact/')

    def test1(self):
        contact_us_message_valid(self.driver)
        time.sleep(0.5)
        element = self.driver.find_element(By.CLASS_NAME, 'uagb-forms-success-message-173d6c98')
        assert not element.is_displayed()

<<<<<<< HEAD
    def test3(self):
        privacy_policy(self.driver)
=======
    def test2(self):
        about_us(self.my_driver)
>>>>>>> 4e13ada5436d841bc8acf779810c024b8879853c
        time.sleep(0.5)


    def tearDown(self) -> None:
        self.driver.close()
