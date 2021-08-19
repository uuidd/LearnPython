#!/bin/python3.7
# coding:utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class ADarkRoom:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_experimental_option("detach", True)  # 不关闭浏览器
        self.driver = webdriver.Chrome()
        self.driver.get("http://adarkroom.doublespeakgames.com/?lang=zh_cn")
        WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located((By.ID, "location_room")))

    def get_event_title(self):
        """
        获取事件标题
        :return: 事件标题文本
        """
        return self.driver.find_element_by_class_name("eventTitle").text

    def click_button_id(self, ele_id):
        """
        点击id属性的按钮
        :param ele_id: 按钮的id名称
        """
        self.get_ele(ele_id).click()

    def click_button(self, ele_id):
        """
        点击按钮，用id定位
        :param ele_id: 按钮的id名称
        """
        if self.driver.find_element_by_id("event"):
            title = self.get_event_title()
            if title == "Sound Available!":
                self.click_button_id("no")
            elif title == "Penrose":
                self.click_button_id("give in")
                self.driver.close()
            elif title == "噪声":
                self.click_button_id("investigate")
                self.click_button_id("backinside")
            elif title == "损毁的陷阱":
                self.click_button_id("track")
                self.click_button_id("end")
            elif title == "神秘流浪者":
                self.click_button_id("deny")
            elif title == "火灾":
                self.click_button_id("mourn")
            elif title == "患病男子":
                self.click_button_id("ignore")
        self.click_button_id(ele_id)

    def get_ele(self, ele_id):
        return WebDriverWait(self.driver, 60).until(ec.visibility_of_element_located((By.ID, ele_id)))

    def go(self):
        self.click_button("lightButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("stokeButton")
        self.click_button("gatherButton")
        self.click_button("build_trap")
        self.click_button("build_cart")
        self.click_button("trapsButton")
        self.click_button("build_hut")


if __name__ == '__main__':
    room = ADarkRoom()
    room.go()
