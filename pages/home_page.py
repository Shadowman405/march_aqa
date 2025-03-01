from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:
    BASE_URL = "https://www.demoblaze.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.BASE_URL)

    def click_s6_link(self):
        s6_link = self.driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        s6_link.click()

    def click_monitors(self):
        monitors_link = self.driver.find_element(By.XPATH, '//a[text()="Monitors"]')
        monitors_link.click()

    def check_monitor_products_count(self, count):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//a[text()="ASUS Full HD"]'))
        )
        monitors_showcase = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors_showcase) == count
