from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pages.create_new_account_page import CreateNewAccountPage
from pages.watches_page import WhatchesPage
from pages.shopping_cart_page import ShoppingCartPage
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    chrome_driver = webdriver.Chrome(options=options)
    actions_element = ActionChains(chrome_driver)
    yield chrome_driver, actions_element
    chrome_driver.quit()

@pytest.fixture()
def watches_page(driver):
    chrome_driver, actions_element = driver
    return WhatchesPage(chrome_driver, actions_element)


@pytest.fixture()
def create_new_account_page(driver):
    chrome_driver, actions_element = driver
    return CreateNewAccountPage(chrome_driver, actions_element)

@pytest.fixture()
def shopping_cart_page(driver):
    chrome_driver, actions_element = driver
    return ShoppingCartPage(chrome_driver, actions_element)