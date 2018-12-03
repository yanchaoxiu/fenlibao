# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\drmgdquc.default'
profile = webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox(profile)
driver.get("http://devdimeng.fenlibao.com/console/common/index.htm")
xp=driver.find_element_by_xpath
xp(".//*[@id='txUserId']").send_keys("admin")
xp(".//*[@id='passwordId']").send_keys("123456")
xp("html/body/div[1]/div[2]/form/div[3]/input").click()
sleep(2)
xp("html/body/div[3]/ul/li[3]/a").click()
sleep(2)
xp("html/body/div[4]/div/div[2]/div/div[2]/div/ul/li[1]/a").click()
sleep(2)
xp(".//*[@id='form_loan']/div/div[1]/div[2]/div[1]/div[2]/a[1]").click()