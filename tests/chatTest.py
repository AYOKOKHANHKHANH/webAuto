import time
import pytest
import unittest
from utils.driversManages import get_driver
from utils.driversManages import chrome_driver_init
from utils.infoLogin import get_url_web
from pages.loginPage import LoginPage
from pages.chatPage import ChatPage
from config.envConfig import EnvConfig


@pytest.mark.usefixtures("driver_class")
class ChatTest(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = get_driver(self.login.browser)
        except Exception as ex:
            print("No param browser", ex)
            self.driver = chrome_driver_init()
        self.url = get_url_web()
        self.driver.get(self.url)
        self.login_obj = LoginPage(self.driver)
        self.list_message = ['fdsh','shcsdk', 'akslclh','nksjbcj']

        envConfig: EnvConfig = EnvConfig.getInstance()
        self.user_name = envConfig.info.user_name
        self.pwd = envConfig.info.pwd
        self.pin = envConfig.info.pin
        self.name_contact = envConfig.info.name_contact
        # self.list_message = envConfig.info.list_message



    def tearDown(self):
        self.driver.quit()

    def login_event(self, username, pwd, pin=None):
        try:
            self.login_obj.click_login_with_halo_acc()

            # Wait load page
            time.sleep(1)

            self.login_obj.enter_username(username)
            self.login_obj.enter_pwd(pwd)
            self.login_obj.click_login()

            if pin is not None:
                self.login_obj.click_continue()
                self.login_obj.enter_pin(pin)
                self.login_obj.click_accept_button()

                time.sleep(1)
                assert self.driver.current_url == self.url


        except Exception as err:
            print("Login unsuccessfully", err)

    def test_chat(self):
        # Login success
        username = self.user_name
        pwd = self.pwd
        pin = self.pin
        self.login_event(username=username, pwd=pwd, pin=pin)

        # Send text for friend
        chat = ChatPage(self.driver)
        chat.click_chat_button()
        chat.enter_search(self.name_contact)
        chat.click_user_to_chat_button()
        try:
            for i in range (len(self.list_message)):
                chat.enter_text_chat(self.list_message[i])
                chat.click_send_button()
        except Exception as error:
            print(error)

    # def test_chat_not_text(self):
    #     username = self.user_name
    #     pwd = self.pwd
    #     pin = self.pin
    #     self.login_event(username=username, pwd=pwd, pin=pin)
    #     chat_not_test = ChatPage(self.driver)
    #     chat_not_test.click_chat_button()
    #     chat_not_test.enter_search(self.name_contact)
    #     chat_not_test.click_user_to_chat_button()
    #     chat_not_test.enter_text_chat("")
    #     chat_not_test.click_send_like_button()


    def test_receive_message(self):
        # Login other account
        username = "0904613192"
        pwd = "blackpinkinyourarea"
        pin = self.pin
        self.login_event(username=username, pwd=pwd, pin=pin)

        # Check message
        check_receive = ChatPage(self.driver)
        check_receive.click_chat_button()
        check_receive.click_user_receive()

        time.sleep(2)
        list_message_receive = check_receive.get_text_message()
        list_message_receive.reverse()
        list_result = []
        for i in range (len(self.list_message)):
            list_result.append(list_message_receive[i])
        list_result.reverse()

        assert list_result == self.list_message