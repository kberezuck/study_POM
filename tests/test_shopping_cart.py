import pytest


@pytest.mark.shopping_cart
def test_empty_shopping_cart(shopping_cart_page):
    shopping_cart_page.open_page()
    shopping_cart_page.check_shopping_cart_empty_block_is_displayed()


@pytest.mark.shopping_cart
def test_link_in_empty_shopping_cart(shopping_cart_page):
    shopping_cart_page.open_page()
    shopping_cart_page.check_shopping_cart_empty_block_is_displayed()
    shopping_cart_page.click_the_here_link()
    shopping_cart_page.check_the_here_link_redirects_to_main_page()


@pytest.mark.shopping_cart
def test_change_amount_of_product(shopping_cart_page, registration_with_valid_data, add_product_to_a_shopping_cart):
    shopping_cart_page.open_page()
    shopping_cart_page.check_shopping_cart_has_products()
    shopping_cart_page.change_amount_of_product()
