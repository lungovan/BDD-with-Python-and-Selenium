from selenium.webdriver.common.by import By


class UploadPage:

    URL = "https://demo.guru99.com/test/upload/"
    FILE_INPUT = (By.CSS_SELECTOR, 'input[type=file]')
    FILE_SIZE_TEXT = (By.XPATH, '//*[@id="uploadwindow"]/span/b')
    TERM_CHECKBOX = (By.ID, "terms")
    TERM_TEXT = (By.XPATH, "//li[@class='col_rgt']//span[@class='field_title']")
    SUBMIT_BUTTON = (By.ID, "submitbutton")
    UPLOAD_SPINNER = (By.XPATH, "//*[@id='submitbutton'][@class='btn buttoncolor has-spinner active']")
    RESPONSE_TEXT = (By.XPATH, '//*[@id="res"][contains(@style,"display: block")]/center')

    def __init__(self, browser):
        self.browser = browser

    def get_file_input_visibility(self):
        return self.browser.find_element(*self.FILE_INPUT).is_displayed()

    def get_file_size_text(self):
        return self.browser.find_element(*self.FILE_SIZE_TEXT).text

    def get_term_text(self):
        return self.browser.find_element(*self.TERM_TEXT).text

    def get_checkbox_is_checked(self):
        return self.browser.find_element(*self.TERM_CHECKBOX).is_selected()

    def get_submit_button_text(self):
        return self.browser.find_element(*self.SUBMIT_BUTTON).text

    def upload_file(self, file_path):
        self.browser.find_element(*self.FILE_INPUT).send_keys(file_path)
        self.browser.find_element(*self.SUBMIT_BUTTON).click()

    def check_upload_spinner_visibility(self):
        return self.browser.find_element(*self.UPLOAD_SPINNER).is_displayed()

    def check_upload_successful_message_text(self):
        return self.browser.find_element(*self.RESPONSE_TEXT).text
