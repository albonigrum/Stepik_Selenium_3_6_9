import time
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


def test_should_check_existence_button_of_add_to_basket(browser: RemoteWebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # time.sleep(30)
    assert browser.find_element_by_css_selector("form#add_to_basket_form button[type=submit]") is not None

