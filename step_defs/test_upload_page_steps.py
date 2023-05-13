from pytest_bdd import scenarios, when, then, parsers, given
from pages.upload import UploadPage
from sttable import parse_str_table

import os

scenarios('../features/upload_page.feature')


@given(parsers.parse('I have navigated to the Upload page'))
def navigate_to(browser):
    url = UploadPage.URL
    browser.get(url)


@then(parsers.parse('The page title is "{title}"'))
def verify_page_title(browser, title):
    assert title == browser.title


@then('The page contains a file input')
def verify_page_title(browser):
    assert UploadPage(browser).get_file_input_visibility() is True


@then(parsers.parse('The page contains text "{text}"'))
def verify_page_title(browser, text):
    assert UploadPage(browser).get_file_size_text() == text


@then(parsers.parse('The page contains a checkbox that is unchecked'))
def verify_page_title(browser):
    assert UploadPage(browser).get_checkbox_is_checked() is False


@then(parsers.parse('The page contains a term text "{text}"'))
def verify_page_title(browser, text):
    assert UploadPage(browser).get_term_text() == text


@then(parsers.parse('The page contains a button "{text}"'))
def verify_page_title(browser, text):
    assert UploadPage(browser).get_submit_button_text() == text


@when("User select a valid file to upload")
def upload_valid_file(browser, assets_path):
    page = UploadPage(browser)
    page.upload_file(os.path.join(assets_path, 'file_upload_valid.txt'))


@then(parsers.parse('The upload spinner displays'))
def verify_spinner_visibility(browser):
    assert UploadPage(browser).check_upload_spinner_visibility() is True


@then(parsers.parse('The page display the upload successful message: "{message}"'))
def verify_successful_message(browser, message):
    if "(newline)" in message:
        message = message.replace("(newline)", "\n")
    assert UploadPage(browser).check_upload_successful_message_text() == message


@when("User select an invalid file to upload that exceed the max size")
def upload_exceed_size_file(browser, assets_path):
    page = UploadPage(browser)
    page.upload_file(os.path.join(assets_path, 'file_upload_exceed.zip'))


# @then(parsers.parse('The page display the error message: "{message}"'))
# def verify_error_message(browser, message):
#     assert 1 == 2
