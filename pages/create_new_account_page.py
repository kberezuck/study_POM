from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CreateNewAccountPage(BasePage):
    page_url = '/customer/account/create/'

    first_name_field = ('xpath', "//input[@id= 'firstname']")
    last_name_field = ('xpath', "//input[@id= 'lastname']")
    email_field = ('xpath', '//input[@id="email_address"]')
    password_field = ('xpath', '//input[@id="password"]')
    confirm_password_field = ('xpath', '//input[@id="password-confirmation"]')
    create_account_button = ('xpath', '//button[@title= "Create an Account"]')
    allert = ('xpath', "//div[@role = 'alert']")
    error_for_requirement_field = ('xpath', "//div[@class = 'mage-error']")

    def click_create_account_button(self):
        self.find_and_click_element(self.create_account_button)

    def clean_all_fields(self):
        self.find_and_clean_field(self.first_name_field)
        self.find_and_clean_field(self.last_name_field)
        self.find_and_clean_field(self.email_field)
        self.find_and_clean_field(self.password_field)
        self.find_and_clean_field(self.confirm_password_field)

    def check_validation_messages(self):
        error_messages = []
        error_elements = self.find_all(self.error_for_requirement_field)

        for element in error_elements:
            error_messages.append(element.text)
            print(element.text)
            self.wait.until(
                EC.text_to_be_present_in_element(self.error_for_requirement_field, 'This is a required field.'))

    def check_success_alert_is_visible(self):
        self.wait.until(
            EC.text_to_be_present_in_element(self.allert, 'Thank you for registering with Main Website Store.'))

    def check_user_is_created(self):
        self.wait.until(EC.url_to_be('https://magento.softwaretestingboard.com/customer/account/'))

    def enter_data_in_first_name_field(self, data):
        self.wait.until(EC.element_to_be_clickable(self.first_name_field)).send_keys(data)
        self.wait.until(EC.text_to_be_present_in_element_value(self.first_name_field, data))

    def enter_data_in_last_name_field(self, data):
        self.wait.until(EC.element_to_be_clickable(self.last_name_field)).send_keys(data)
        self.wait.until(EC.text_to_be_present_in_element_value(self.last_name_field, data))

    def enter_data_in_email_field(self, data):
        self.wait.until(EC.element_to_be_clickable(self.email_field)).send_keys(data)
        self.wait.until(EC.text_to_be_present_in_element_value(self.email_field, data))

    def enter_data_in_password_field(self, data):
        self.wait.until(EC.element_to_be_clickable(self.password_field)).send_keys(data)
        self.wait.until(EC.text_to_be_present_in_element_value(self.password_field, data))

    def enter_data_in_confirm_password_field(self, data):
        self.wait.until(EC.element_to_be_clickable(self.confirm_password_field)).send_keys(data)
        self.wait.until(EC.text_to_be_present_in_element_value(self.confirm_password_field, data))

    def fill_all_field_with_valid_data(self, first_name, last_name, email, password):
        self.enter_data_in_first_name_field(first_name)
        self.enter_data_in_last_name_field(last_name)
        self.enter_data_in_email_field(email)
        self.enter_data_in_password_field(password)
        self.enter_data_in_confirm_password_field(password)
