# coding:utf-8
from appium import webdriver
from time import sleep

deviceName='9b57e6c57cf3'
platformVersion='6.0.1'

desired_caps = {
    'platformName': 'Android',
    'deviceName': deviceName,
    'platformVersion': platformVersion,
    'appPackage': 'com.fenlibao.fenlibao',
    'appActivity': 'com.fenlibao.fenlibao.common.activity.SplashActivity',
    'noReset': 'true',
    'resetKeyboard': 'true',
    'unicodeKeyboard': 'true'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(20)


driver.tap([(836,566)],100)
driver.find_element_by_xpath("//android.widget.ImageView[@resource-id=\"com.fenlibao.fenlibao:id/iv_wealth_cg\"]").click()
sleep(1)
driver.find_element_by_xpath("//android.widget.EditText[@resource-id=\"com.fenlibao.fenlibao:id/et_password\"]").send_keys("574098")
sleep(1)
driver.find_element_by_xpath("//android.widget.Button[@resource-id=\"com.fenlibao.fenlibao:id/btn_submit\"]").click()



