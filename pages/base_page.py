from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    host_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver, actions: ActionChains):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5, poll_frequency=1)
        self.actions = actions

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.host_url}{self.page_url}')
        else:
            raise NotImplementedError ('Can not open page')

    def find(self, locator):
        return self.driver.find_elements(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def find_and_clean_field(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).clear()

    def find_and_click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()








