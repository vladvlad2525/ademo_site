from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

url = 'https://thedemosite.co.uk/'


<<<<<<< HEAD
=======
url = 'https://thedemosite.co.uk/contact/'
>>>>>>> 4e13ada5436d841bc8acf779810c024b8879853c
def driver_setup():
    options = ChromeOptions()
    options.add_experimental_option('detach', True)
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


driver = driver_setup()

if __name__ == '__main__':
    driver.get(url)
