# -*- coding: utf-8 -*-

from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


def create_screenshot(urls, scr_name, sleep=10, proxys=None):
    if proxys is not None:
        proxy = proxys
        firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        firefox_capabilities['proxy'] = {
            "proxyType": "MANUAL",
            "httpProxy": proxy,
            "ftpProxy": proxy,
            "sslProxy": proxy
        }
        driver = webdriver.Firefox(capabilities=firefox_capabilities)
        driver.maximize_window()
        driver.get(url=urls)
        time.sleep(sleep)
        try:
            WebDriverWait(driver, 10)
        finally:
            img = ImageGrab.grab()
            screenshot_name = str(scr_name) + '.png'
            img.save(screenshot_name)
            driver.quit()
    else:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url=urls)
        time.sleep(sleep)
        try:
            WebDriverWait(driver, 10)
        finally:
            img = ImageGrab.grab()
            screenshot_name = str(scr_name) + '.png'
            img.save(screenshot_name)
            driver.quit()


count = 0
with open(file='input.txt', mode='r', encoding='utf-8') as file:
    for url in file:
        url = url.replace('\n', '')
        count += 1
        screen_name = 'Mon3_' + str(count)
        create_screenshot(urls=url, scr_name=screen_name, proxys=None, sleep=0)
