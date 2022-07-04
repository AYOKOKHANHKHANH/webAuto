import time
import pytest
import unittest
from config.envConfig import EnvConfig
from pages.LoginPage.loginPage import LoginPage
from pages.GroupPage.createGroupPage import CreateGroupPage
from utils.driversManages import chrome_driver_init
from utils.driversManages import get_driver
from utils.infoLogin import get_url_web


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

        envConfig : EnvConfig = EnvConfig.getInstance()
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

        except Exception as err:
            print("Login unsuccessfully", err)

    def test_create_group(self):
        """
        - Click group button
        - Click create grou button
        - Enter name group
        - Click ok button
        :return: Compare first name group in list group with name group and length of list before and after

        """
        self.login_event()
        print(self.name_group)

        self.create_group.click_group_button()
        list_group_before = self.create_group.get_list_group()
        self.create_group.click_create_group_button()
        self.create_group.enter_name_group(self.name_group)

        # create_group.click_close_button()
        self.create_group.click_ok_button()
        self.create_group.click_invite_button()
        list_group_after = self.create_group.get_list_group()

        assert len(list_group_before) + 1 == len(list_group_after)
        assert self.name_group == self.create_group.get_first_group_in_list_group()

    def test_create_group_not_enter_name_group(self):
        """
            - Click group button
            - Click create button
            - Click ok
        :return: Button ok disable
        """

        self.login_event()
        self.create_group.click_group_button()
        self.create_group.click_create_group_button()
        assert self.create_group.click_ok_button() is None

    def test_create_group_but_click_cancel(self):
        """
            - Click group button
            - Click create group
            - Click close button
        :return: length of before list == length of after list
        """
        self.login_event()
        self.create_group.click_group_button()
        list_group_before = self.create_group.get_list_group()
        self.create_group.click_create_group_button()
        self.create_group.click_close_button()
        list_group_after = self.create_group.get_list_group()
        assert len(list_group_before) == len(list_group_after)

    def test_del_group(self):
        """
        - Click group button
        - Click option button
        - Click delete button
        - Click ok button
        :return: length of current list - 1 == length of list after delete
        """
        self.login_event()
        self.create_group.click_group_button()
        list_group_before = self.create_group.get_list_group()
        # i = 1
        try:
            self.create_group.click_option_button()
            self.create_group.click_del_group_button()
            self.create_group.click_ok_button()
            list_group_after = self.create_group.get_list_group()

            assert len(list_group_after) == len(list_group_before) - 1
            # while i < (len(self.create_group.get_list_group())):
            #     self.create_group.click_option_button()
            #     self.create_group.click_del_group_button()
            #     self.create_group.click_ok_button()
            #     i += 1
        except Exception as e:
            print(e)


    def test_on_noti(self):
        """
        - Click group button
        - Click option button
        - Click on notification button
        - Click ok button
        :return: Text == Tắt thông báo
        """
        self.login_event()
        self.create_group.click_group_button()
        try:
            self.create_group.click_option_button()
            self.create_group.click_on_noti_button()
            self.create_group.click_ok_button()

            self.create_group.click_option_button()
            assert self.create_group.get_text_off_noti_button() == "Tắt thông báo"
        except Exception as e:
            print(e)
        # self.create_group.click_close_button()

    def test_off_noti(self):
        """
        - Click group button
        - Click option button
        - Click on button
        - Click ok button
        - Click option button
        - Click off button
        - Click ok button
        :return: Text == Bật thông báo
        """
        self.login_event()
        self.create_group.click_group_button()
        try:
            self.create_group.click_option_button()
            self.create_group.click_on_noti_button()
            self.create_group.click_ok_button()
            self.create_group.click_option_button()
            self.create_group.click_off_noti_button()
            self.create_group.click_ok_button()
            self.create_group.click_option_button()
            assert self.create_group.get_text_on_noti_button() == "Bật thông báo"
        except Exception:
            print(Exception)


    def test_add_friend_to_group(self):
        """
        - Click group button
        - Click option button
        - Click add friend to group
        - Enter name of user which want to add friend
        - Click invite button
        :return:
        """
        self.login_event()

        self.create_group.click_group_button()
        print(self.name_contact)
        try:
            self.create_group.click_option_button()
            self.create_group.click_add_friend_to_group_button()
            self.create_group.enter_name_user(self.name_contact)
            self.create_group.click_invite_button()
            assert self.create_group.click_invite_button() is None

        except Exception as s:
            print(s)
