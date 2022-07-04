from locators.GroupLocator.createGroupLocator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CreateGroupPage:
    def __init__(self,driver):
        self.driver = driver

    def click_group_button(self):
        print("Click group button")
        # group_button = self.driver.find_element(By.ID,get_group_button_id())
        group_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_group_button_id())))
        group_button.click()

    def click_create_group_button(self):
        print("Click create group button")
        # add_channel_button = self.driver.find_element_by_id(get_add_channel_button_id())
        add_channel_button = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, get_add_channel_button_id())))
        add_channel_button.click()

    def enter_name_group(self,name_grp):
        print("Enter name group")
        # name_group = self.driver.find_element_by_xpath(get_group_name_xpath())
        name_group = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, get_group_name_xpath())))
        name_group.send_keys(name_grp)

    def click_ok_button(self):
        print("Click ok button")
        ok_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_ok_button_id())))
        # ok_button = self.driver.find_element_by_id(get_ok_button_id())
        ok_button.click()

    def click_close_button(self):
        print("Click close button")
        # close_button = self.driver.find_element_by_id(get_close_button_id())
        close_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, get_close_button_id())))
        close_button.click()

    def enter_name_user(self,name_contact):
        print("Enter name contact")
        # name_user = self.driver.find_element_by_xpath(get_group_name_xpath())
        name_user = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,get_search_name_user_xpath())))
        name_user.send_keys(name_contact)

    def click_invite_button(self):
        print("Click invite button")
        # invite_button = self.driver.find_element_by_xpath(get_invite_button_xpath())
        invite_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, get_invite_button_xpath())))
        invite_button.click()

    def click_option_button(self):
        print("Click option button")
        # option_button = self.driver.find_element_by_xpath(get_option_button_xpath())
        option_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, get_option_button_xpath())))
        option_button.click()

    def click_add_friend_to_group_button(self):
        print("Click add friend to group button")
        # add_friend_to_group_button = self.driver.find_element_by_id(get_add_friend_to_group_button_id())
        add_friend_to_group_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_add_friend_to_group_button_css())))
        add_friend_to_group_button.click()

    def click_on_noti_button(self):
        print("Click on noti button")
        # on_off_noti_button = self.driver.find_element_by_id(get_on_off_noti_button_xpath())
        on_noti_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_on_noti_button_css())))
        on_noti_button.click()

    def get_text_off_noti_button(self):
        text_off_noti = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR, get_off_noti_button_css())))
        return text_off_noti.text

    def click_off_noti_button(self):
        print("Click off noti button")
        # on_off_noti_button = self.driver.find_element_by_id(get_on_off_noti_button_xpath())
        off_noti_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_off_noti_button_css())))
        off_noti_button.click()

    def get_text_on_noti_button(self):
        text_on_button = WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located((By.CSS_SELECTOR, get_on_noti_button_css())))
        return text_on_button.text

    def click_del_group_button(self):
        print("Click del_group_button")
        # del_group_button = self.driver.find_element_by_xpath(get_del_group_button_xpath())
        del_group_button = WebDriverWait(self.driver, 500).until(EC.element_to_be_clickable((By.CSS_SELECTOR,get_del_group_button_css())))
        del_group_button.click()

    def get_list_group(self):
        print("Get list group")
        list = []
        # list_group = self.driver.find_elements(By.CSS_SELECTOR, get_list_group_class())
        list_group = WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, get_list_group_class())))
        for elt in list_group:
            list.append(elt.text)
        return list

    def get_first_group_in_list_group(self):
        print("Get first group in list group")
        group = WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.XPATH, get_first_group_in_list_group())))
        return group.text

    def click_X_button(self):
        print("Click X button")
        X_button = self.driver.find_element(By.XPATH,get_X_button_class())
        X_button.click()