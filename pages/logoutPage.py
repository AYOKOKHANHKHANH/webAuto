from locators.logoutLocator import *


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_avatar(self):
        avt = self.driver.find_element_by_xpath(get_avt_btn_xpath())
        avt.click()

    def click_avatar_not_img(self):
        print("Click avatar not image")
        avatar_not_img = self.driver.find_element_by_xpath(get_avatar_not_img())
        avatar_not_img.click()

    def click_logout(self):
        logout_btn = self.driver.find_element_by_xpath(get_logout_btn_xpath())
        logout_btn.click()

    def click_ok(self):
        ok_btn = self.driver.find_element_by_id(get_ok_btn_id())
        ok_btn.click()
