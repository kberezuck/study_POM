import time

import pytest


@pytest.fixture()
def registration_with_valid_data(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.clean_all_fields()
    create_new_account_page.fill_all_field_with_valid_data('test37', 'konor', 'test37@mailto.plus', 'Qwerty1234')
    create_new_account_page.click_create_account_button()
    time.sleep(5)
    create_new_account_page.check_user_is_created()
    create_new_account_page.check_success_alert_is_visible()


@pytest.fixture()
def add_product_to_a_shopping_cart(watches_page):
    watches_page.move_cursor_to_gear_shop_category_and_click_on_watches()
    watches_page.add_product_to_a_shopping_cart()
    watches_page.check_that_button_had_added_status()






