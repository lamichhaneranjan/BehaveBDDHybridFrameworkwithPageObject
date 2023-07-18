from features.pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_product_link_text = "HP LP3065"
    message_css_selector = "body > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > p:nth-child(7)"
    def display_status_of_product(self):
        return self.display_status("valid_product_link_text", self.valid_product_link_text)

    def display_status_of_message(self, expected_message_text):
        return self.retrieved_element_text_equals("message_css_selector", self.message_css_selector, expected_message_text)
