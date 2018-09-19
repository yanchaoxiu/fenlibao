# coding:utf-8
from appium import webdriver
from time import sleep


desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '4.4.2',
    'appPackage': 'com.fenlibao.fenlibao.debug236',
    'appActivity': 'com.fenlibao.fenlibao.common.activity.SplashActivity',
    'noReset': 'true',
    'resetKeyboard': 'true',
    'unicodeKeyboard': 'true'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(20)


