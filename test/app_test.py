from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_move_to_s6(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_s6_link()
    product_page = ProductPage(driver)
    product_page.check_title_is("Samsung galaxy s6")


def test_two_monitors_in_section(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_monitors()
    home_page.check_monitor_products_count(2)
