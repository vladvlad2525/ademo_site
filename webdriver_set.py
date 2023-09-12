from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


url = 'https://thedemosite.co.uk/contact/'
def driver_setup():
    options = ChromeOptions()
    options.add_experimental_option('detach', True)
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

if __name__ == '__main__':
   driver_setup().get(url)
