import time

import pytest


@pytest.mark.watches_page
def test_add_product_to_wish_list_no_authorization_user(watches_page):
    watches_page.open_page()
    watches_page.move_cursor_to_a_card()
    watches_page.add_to_wishlist_button_is_displayed_and_click_on_the_button()
    watches_page.check_redirect_to_logIN_page()
    watches_page.check_the_alert_message_is_displayed_on_logIN_page()
    watches_page.check_login_page_title()
    time.sleep(5)


@pytest.mark.watches_page
def test_add_product_to_wish_list_user_is_authorized(watches_page, registration_with_valid_data):
    watches_page.move_cursor_to_gear_shop_category_and_click_on_watches()
    watches_page.move_cursor_to_a_card()
    watches_page.add_to_wishlist_button_is_displayed_and_click_on_the_button()
    watches_page.check_that_wishlist_page_is_opened()
    watches_page.check_the_alert_message_is_displayed_on_whishlist_page()
