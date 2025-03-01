from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def check_title_is(self, title):
        page_title = self.driver.find_element(By.CLASS_NAME, "name")
        assert page_title.text == title
