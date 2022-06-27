import time
import pytest
import unittest
from config.envConfig import EnvConfig
from pages.loginPage import LoginPage
from pages.createGroupPage import CreateGroupPage
from utils.driversManages import chrome_driver_init
from utils.driversManages import get_driver
from utils.infoLogin import get_url_web
from selenium.common.exceptions import ElementClickInterceptedException


@pytest.mark.usefixtures("driver_class")
class CreateGroup(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = get_driver(self.login.browser)
        except Exception as ex:
            print("No param browser", ex)
            self.driver = chrome_driver_init()
        self.url = get_url_web()
        self.driver.get(self.url)
        self.login_obj = LoginPage(self.driver)
        self.create_group = CreateGroupPage(self.driver)

        envConfig: EnvConfig = EnvConfig.getInstance()
        self.user_name = envConfig.info.user_name
        self.pwd = envConfig.info.pwd
        self.pin = envConfig.info.pin
        self.name_contact = envConfig.info.name_contact
        self.name_group = envConfig.info.name_group

    def tearDown(self):
        self.driver.quit()

    def login_event(self):
        try:
            self.login_obj.click_login_with_halo_acc()

            # Wait load page
            time.sleep(1)
            username = self.user_name
            pwd = self.pwd
            pin = self.pin
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

    # def test_create_group(self):
    #     self.login_event()
    #     print(self.name_group)
    #
    #     self.create_group.click_group_button()
    #     self.create_group.click_create_group_button()
    #     self.create_group.enter_name_group(self.name_group)
    #     # create_group.click_close_button()
    #     self.create_group.click_ok_button()
    #     self.create_group.click_invite_button()
    #     self.create_group.click_close_button()
    #
    #     list_group = self.create_group.get_list_group()
    #     assert list_group[0] == self.name_group
    #
    def test_del_group(self):
        self.login_event()
        self.create_group.click_group_button()
        i = 1
        try:
            self.create_group.click_option_button()
            self.create_group.click_del_group_button()
            self.create_group.click_ok_button()
            # while i < (len(self.create_group.get_list_group())):
            #     self.create_group.click_option_button()
            #     self.create_group.click_del_group_button()
            #     self.create_group.click_ok_button()
            #     i += 1

        except Exception as e:
            # while i < (len(self.create_group.get_list_group())):
            #     self.create_group.click_option_button()
            #     self.create_group.click_del_group_button()
            #     self.create_group.click_ok_button()
            #     i += 1
            print(e)

    #
    #     # self.create_group.click_close_button()
    #
    # def test_on_off_noti(self):
    #     self.login_event()
    #     self.create_group.click_group_button()
    #     try:
    #         self.create_group.click_option_button()
    #
    #         try:
    #             self.create_group.click_off_noti_button()
    #         except Exception as r:
    #             self.create_group.click_on_noti_button()
    #         self.create_group.click_ok_button()
    #         # print(self.create_group.get_text_on_off_noti_button())
    #     except Exception as e:
    #         print(e)
    #     # self.create_group.click_close_button()

    # def test_add_friend_to_group(self):
    #     self.login_event()
    #
    #     self.create_group.click_group_button()
    #     print(self.name_contact)
    #     try:
    #         self.create_group.click_option_button()
    #
    #         self.create_group.click_add_friend_to_group_button()
    #
    #         self.create_group.enter_name_user(self.name_contact)
    #         self.create_group.click_invite_button()
    #
    #     except Exception as s:
    #         print(s)
    #
    #     assert self.create_group.click_invite_button() == None
    #         # self.create_group.click_close_button()
