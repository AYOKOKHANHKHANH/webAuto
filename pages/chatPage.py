from locators.chatLocator import *


class ChatPage:
    def __init__(self,driver):
        self.driver = driver

    def click_chat_button(self):
        print("Click chat button")
        chat_button = self.driver.find_element_by_xpath(get_chat_button_xpath())
        chat_button.click()

    def enter_search(self,name_contact):
        print("Click search button")
        search = self.driver.find_element_by_xpath(get_search_xpath())
        search.send_keys(name_contact)

    def click_user_to_chat_button(self):
        print("Click button to chat")
        user_to_chat = self.driver.find_element_by_xpath(get_user_to_chat_button_xpath())
        user_to_chat.click()

    def enter_text_chat(self, text):
        print("Enter text chat")
        text_chat = self.driver.find_element_by_xpath(get_input_text_chat_xpath())
        text_chat.send_keys(text)

    def click_send_button(self):
        print("Click send button")
        send_button = self.driver.find_element_by_id(get_send_button_id())
        send_button.click()

    def click_send_like_button(self):
        print("Click send like button")
        send_like_button = self.driver.find_element_by_id(get_send_like_button_id())
        send_like_button.click()

    def click_hello_start_button(self):
        print("Click hello start button")
        hello_start_button = self.driver.find_element_by_xpath(get_hello_start_button_xpath())
        hello_start_button.click()

    def click_emoji_chat_button(self):
        print("Click emoji chat button")
        emoji_chat_button = self.driver.find_element_by_xpath(get_emoji_chat_button_id())
        emoji_chat_button.click()

    def click_emoji_button(self):
        print("Click emoji button")
        emoji_button = self.driver.find_element_by_xpath(get_emoji_button_xpath())
        emoji_button.click()

    def get_text_message(self):
        print("get text message")
        text_message = self.driver.find_element_by_class_name(get_text_message()).text
        return text_message
