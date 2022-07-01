from locators.ChatLocator.chatLocator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChatPage:
    def __init__(self,driver):
        self.driver = driver

    def click_chat_button(self):
        print("Click chat button")
        # chat_button = self.driver.find_element_by_xpath(get_chat_button_xpath())
        chat_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, get_chat_button_xpath())))
        chat_button.click()

    def enter_search(self,name_contact):
        print("Click search button")
        # search = self.driver.find_element_by_xpath(get_search_xpath())
        search = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, get_search_xpath())))
        search.send_keys(name_contact)

    def click_user_to_chat_button(self):
        print("Click button to chat")
        # user_to_chat = self.driver.find_element_by_xpath(get_user_to_chat_button_xpath())
        user_to_chat = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, get_user_to_chat_button_xpath())))
        user_to_chat.click()

    def enter_text_chat(self, text):
        print("Enter text chat")
        # text_chat = self.driver.find_element_by_xpath(get_input_text_chat_xpath())
        text_chat = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,get_input_text_chat_xpath())))
        text_chat.send_keys(text)

    def click_send_button(self):
        print("Click send button")
        # send_button = self.driver.find_element_by_id(get_send_button_id())
        send_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_send_button_id())))
        send_button.click()

    def click_send_like_button(self):
        print("Click send like button")
        # send_like_button = self.driver.find_element_by_id(get_send_like_button_id())
        send_like_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_send_like_button_id())))
        send_like_button.click()

    def click_hello_start_button(self):
        print("Click hello start button")
        # hello_start_button = self.driver.find_element_by_xpath(get_hello_start_button_xpath())
        hello_start_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, get_hello_start_button_xpath())))
        hello_start_button.click()

    def click_emoji_chat_button(self):
        print("Click emoji chat button")
        # emoji_chat_button = self.driver.find_element_by_xpath(get_emoji_chat_button_id())
        emoji_chat_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, get_emoji_chat_button_id())))
        emoji_chat_button.click()

    def click_emoji_button(self):
        print("Click emoji button")
        # emoji_button = self.driver.find_element_by_xpath(get_emoji_button_xpath())
        emoji_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, get_emoji_button_xpath())))
        emoji_button.click()

    def get_text_message(self):
        list_message_receive = []
        print("get text message")
        # text_message_receive = self.driver.find_elements(By.CSS_SELECTOR, get_text_message())
        text_message_receive = WebDriverWait(self.driver, 90).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, get_text_message())))
        for elt in text_message_receive:
            list_message_receive.append(elt.text)
        return list_message_receive

    def click_user_receive(self):
        print("Click user receive")
        # user_receive = self.driver.find_element_by_xpath(get_receive_user_click_xpath())
        user_receive = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, get_receive_user_click_xpath())))
        user_receive.click()