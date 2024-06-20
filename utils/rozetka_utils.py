from selenium.webdriver.common.by import By
import re
from utils.web_driver import CustomWebDriver


class RozetkaUtils:
    def __init__(self):
        self.url = "https://rozetka.com.ua/"
        self.custom_driver = CustomWebDriver()
        self.search_icon = (By.XPATH, "//button[contains(@class, 'search-form__submit')]")
        self.search_input = (By.XPATH, "//input[@name='search']")
        self.search_title = (By.XPATH, "//h1[@class='catalog-heading ng-star-inserted']")
        self.search_item_grid = (By.XPATH, "//li[contains(@class,'catalog-grid')]//a[contains(@title,'%s')]")
        self.main_item_title = (By.XPATH, "//h1[@class='product__title']")
        self.prod_prc = (By.XPATH, "//div[contains(@class, 'product-price')]//p[contains(@class, 'product-price__big')]")
        self.buy_button = (By.XPATH, "//rz-product-buy-btn[contains(@class, 'product-button__buy')]//button")
        self.current_prod_price = (By.XPATH, "//div[contains(@class, 'cart-receipt__sum-price')]//span")
        self.current_item_title = (By.XPATH, "//div[contains(@class, 'cart-product__main')]//a")
        self.error_message = (By.XPATH, "")


    def open_rozetka_page(self):
        self.custom_driver.open_url(self.url)

    def search_item(self, search_text):
        self.custom_driver.input_text(self.search_input, search_text)
        self.custom_driver.click_web_element(self.search_icon)
        current_title = self.custom_driver.wait_web_element(self.search_title).text
        current_title = current_title.replace('«', '').replace('»', '')
        # current_title = re.match()
        assert search_text == current_title, f"Actual title: {current_title} doesn't match with expected: {search_text}"

    def select_item_from_grid(self, text: str):
        selector = self.custom_driver.format_selector(self.search_item_grid, text)
        item_title_search = self.custom_driver.get_attribute_text(selector)
        clickable_element = f"{selector[1]}//.."
        selector = list(selector)
        selector[1] = clickable_element
        selector = tuple(selector)
        self.custom_driver.click_web_element(selector)
        self.title = self.custom_driver.wait_web_element(self.main_item_title).text
        assert item_title_search == self.title, f"Actual title: {self.title} doesn't match with expected: {item_title_search}"

    def validate_selected_product_in_cart(self):
        price_on_page = self.custom_driver.wait_web_element(self.prod_prc).text
        self.custom_driver.click_web_element(self.buy_button)
        current_price = self.custom_driver.wait_web_element(self.current_prod_price).text
        current_title = self.custom_driver.wait_web_element(self.current_item_title).text
        assert price_on_page == current_price, f"Actual price: {current_price} doesn't match with expected: {price_on_page}"
        assert self.title == current_title, f"Actual item: {current_title} doesn't match with expected: {self.title}"

    def search_item_camelcase (self, search_text: str, success=True):
        self.custom_driver.input_text(self.search_input, search_text)
        self.custom_driver.click_web_element(self.search_icon)
        if success:
            current_title = self.custom_driver.wait_web_element(self.search_title).text
            current_title = current_title.replace('«', '').replace('»', '')
            assert search_text == current_title, f"Actual title: {current_title} doesn't match with expected: {search_text}"
            return current_title
        else:
            self.custom_driver = self.custom_driver.wait_web_element(self.error_message)
