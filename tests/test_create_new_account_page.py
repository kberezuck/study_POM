import pytest


@pytest.mark.create_new_account_page
def test_leave_all_field_empty(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.clean_all_fields()
    create_new_account_page.click_create_account_button()
    create_new_account_page.check_validation_messages()


@pytest.mark.create_new_account_page
def test_fill_email_field(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.clean_all_fields()
    create_new_account_page.enter_data_in_email_field('bla-bla@mail.ru')


@pytest.mark.create_new_account_page
def test_registration_with_valid_data(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.clean_all_fields()
    create_new_account_page.fill_all_field_with_valid_data('test38', 'konor', 'test38@mailto.plus', 'Qwerty1234')
    create_new_account_page.click_create_account_button()
    create_new_account_page.check_user_is_created()
    create_new_account_page.check_success_alert_is_visible()
