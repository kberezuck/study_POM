from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class WhatchesPage(BasePage):
    page_url = '/gear/watches.html'

    first_product_card = ('xpath', "//ol[@class = 'products list items product-items']/li[1]")
    add_to_wishlist_button = ('xpath', "(//a[@class = 'action towishlist'])[1]")
    customer_page_title = ('xpath', '//title')
    alert = ('xpath', "//div[@role='alert']")
    gear_shop_category = ('xpath', "//li[@class = 'level0 nav-4 category-item level-top parent ui-menu-item']")
    watches_shop_category_from_gear = (
        'xpath',
        "//li[@class = 'level0 nav-4 category-item level-top parent ui-menu-item']//li[contains(@class, 'last')]")

    second_product_card = ('xpath', "//ol[@class = 'products list items product-items']/li[2]")
    add_to_cart_button = ('xpath', '//form[@data-product-sku="24-WG03"]/button')

    added_status_of_cart_button = ('xpath', "//form[@data-product-sku='24-WG03']/button/span")

    counter_of_shopping_cart = ('xpath', "//input[@id = 'cart-493204-qty']")

    def move_cursor_to_a_card(self):
        self.actions.move_to_element(self.driver.find_element(*self.first_product_card)).perform()

    def check_redirect_to_logIN_page(self):
        self.wait.until(EC.url_contains('https://magento.softwaretestingboard.com/customer/account/login/referer'))

    def check_login_page_title(self):
        self.wait.until(EC.title_is('Customer Login'))
        print(self.driver.find_element(*self.customer_page_title).text)

    def check_the_alert_message_is_displayed_on_logIN_page(self):
        self.wait.until(EC.presence_of_element_located(self.alert))
        self.wait.until(
            EC.text_to_be_present_in_element(self.alert, 'You must login or register to add items to your wishlist.'))
        print(self.driver.find_element(*self.alert).text)

    def add_to_wishlist_button_is_displayed_and_click_on_the_button(self):
        self.wait.until(EC.element_to_be_clickable(self.add_to_wishlist_button))
        self.find_and_click_element(self.add_to_wishlist_button)

    def move_cursor_to_gear_shop_category_and_click_on_watches(self):
        self.wait.until(EC.element_to_be_clickable(self.gear_shop_category))
        self.actions.move_to_element(self.driver.find_element(*self.gear_shop_category)) \
            .move_to_element(self.driver.find_element(*self.watches_shop_category_from_gear)) \
            .perform()
        self.driver.find_element(*self.watches_shop_category_from_gear).click()
        self.wait.until(EC.url_to_be('https://magento.softwaretestingboard.com/gear/watches.html'))

    def check_that_wishlist_page_is_opened(self):
        self.wait.until(EC.url_contains('/wishlist/index/index/wishlist_id'))

    def check_the_alert_message_is_displayed_on_whishlist_page(self):
        self.wait.until(EC.presence_of_element_located(self.alert))
        self.wait.until(
            EC.text_to_be_present_in_element(self.alert,
                                             'Didi Sport Watch has been added to your Wish List. Click here to continue shopping.'))
        print(self.driver.find_element(*self.alert).text)

    def get_current_state_of_shopping_cart_counter(self):
        self.find_and_click_element(self.counter_of_shopping_cart)
        current_counter = self.driver.find_element(*self.counter_of_shopping_cart).text
        print(current_counter)

    def add_product_to_a_shopping_cart(self):
        self.actions.move_to_element(self.driver.find_element(*self.second_product_card)).perform()
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart_button))
        self.find_and_click_element(self.add_to_cart_button)

    def check_that_button_had_added_status(self):
        self.wait.until(EC.text_to_be_present_in_element(self.added_status_of_cart_button, 'Added'))
