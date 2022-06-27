from locators.logoutLocator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_avatar(self):
        print("Click avatar")
        avt = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, get_avt_btn_xpath())))
        avt.click()

    def click_avatar_not_img(self):
        print("Click avatar not image")
        avatar_not_img = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,get_avatar_not_img())))
        avatar_not_img.click()

    def click_logout(self):
        print("Click log out")
        logout_btn = self.driver.find_element_by_xpath(get_logout_btn_xpath())
        logout_btn.click()

    def click_ok(self):
        print("Click ok")
        ok_btn = self.driver.find_element_by_id(get_ok_btn_id())
        ok_btn.click()
