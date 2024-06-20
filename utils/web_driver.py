from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomWebDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.timeout = 30

    def open_url(self, url):
        self.driver.get(url)

    def wait_web_element(self, element):
        wait_lib = WebDriverWait(self.driver, self.timeout)
        web_element = wait_lib.until(EC.presence_of_element_located((element[0], element[1])))
        return web_element

    def click_web_element(self, element):
       elem = self.wait_web_element(element)
       elem.click()

    def input_text(self, element, text):
       elem = self.wait_web_element(element)
       elem.send_keys(text)

    @staticmethod
    def format_selector(selector, text):
        selector_formatted = (selector[0], selector[1] % text)
        return selector_formatted

    def get_attribute_text(self, selector, attribute='title'):
        elem = self.wait_web_element(selector)
        attribute_text = elem.get_attribute(attribute)
        return attribute_text