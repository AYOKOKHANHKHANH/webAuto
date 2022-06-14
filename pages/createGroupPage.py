from locators.createGroupLocator import *

class CreateGroupPage:
    def __init__(self,driver):
        self.driver = driver

    def click_group_button(self):
        print("Click group button")
        group_button = self.driver.find_element_by_id(get_group_button_id())
        group_button.click()

    def click_add_channel_button(self):
        print("Click create group button")
        add_channel_button = self.driver.find_element_by_id(get_add_channel_button_id())
        add_channel_button.click()

    def enter_name_group(self,name_grp):
        print("Enter name group")
        name_group = self.driver.find_element_by_xpath(get_group_name_xpath())
        name_group.send_keys(name_grp)

    def click_ok_button(self):
        print("Click ok button")
        ok_button = self.driver.find_element_by_id(get_ok_button_id())
        ok_button.click()

    def click_close_button(self):
        print("Click close button")
        close_button = self.driver.find_element_by_id(get_close_button_id())
        close_button.click()

    def enter_name_user(self,name_contact):
        print("Enter name contact")
        name_user = self.driver.find_element_by_xpath(get_search_name_user_xpath())
        name_user.send_keys(name_contact)

    def click_invite_button(self):
        print("Click invite button")
        invite_button = self.driver.find_element_by_xpath(get_invite_button_xpath())
        invite_button.click()

    def click_option_button(self):
        print("Click option button")
        option_button = self.driver.find_element_by_xpath(get_option_button_xpath())
        option_button.click()

    def click_add_friend_to_group_button(self):
        print("Click add friend to group button")
        add_friend_to_group_button = self.driver.find_element_by_xpath(get_add_friend_to_group_button_xpath())
        add_friend_to_group_button.click()

    def click_on_off_noti_button(self):
        print("Click on_off_noti_button")
        on_off_noti_button = self.driver.find_element_by_xpath(get_on_off_noti_button_xpath())
        on_off_noti_button.click()

    def click_del_group_button(self):
        print("Click del_group_button")
        del_group_button = self.driver.find_element_by_xpath(get_del_group_button_xpath())
        del_group_button.click()
