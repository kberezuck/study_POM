from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    page_url = '/checkout/cart/'

    here_link = ('xpath', "//div[@class = 'cart-empty']//a")
    empty_cart_block = ('xpath', '//div[@class = "cart-empty"]')
    shopping_cart_table = ('xpath', "//table[@id = 'shopping-cart-table']")
    amount_of_product = ('xpath', "//input[@title = 'Qty']")
    update_shopping_cart_button = ('xpath', "//button[@title='Update Shopping Cart']")
    subtotal_price = ('xpath', "//td[@class = 'col subtotal']")
    finish_subtotal = ('xpath', "//tr[@class='totals sub']")

    loading_state = ('xpath', "//div[@class ='loading-mask']")

    def check_shopping_cart_empty_block_is_displayed(self):
        empty_cart_text = self.driver.find_element(*self.empty_cart_block).text
        print(empty_cart_text)
        self.wait.until(EC.text_to_be_present_in_element(self.empty_cart_block, empty_cart_text))

    def click_the_here_link(self):
        self.wait.until(EC.element_to_be_clickable(self.here_link))
        self.find_and_click_element(self.here_link)

    def check_the_here_link_redirects_to_main_page(self):
        self.wait.until(EC.url_to_be('https://magento.softwaretestingboard.com/'))

    def check_shopping_cart_has_products(self):
        self.wait.until(EC.visibility_of_element_located(self.shopping_cart_table))

    def change_amount_of_product(self):
        initial_subtotal = self.driver.find_element(*self.subtotal_price).text
        print(initial_subtotal)
        self.wait.until(EC.element_to_be_clickable(self.amount_of_product))
        self.find_and_clean_field(self.amount_of_product)
        self.driver.find_element(*self.amount_of_product).send_keys('5')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.find_and_click_element(self.update_shopping_cart_button)
        self.wait.until(EC.visibility_of_element_located(self.loading_state))
        self.wait.until(EC.visibility_of_element_located(self.finish_subtotal))
        finish_subtotal = self.driver.find_element(*self.finish_subtotal).text
        print(finish_subtotal)
        assert initial_subtotal != finish_subtotal, 'update button does not work'
