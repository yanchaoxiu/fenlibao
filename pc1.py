# coding:utf-8
from selenium import webdriver
from time import sleep
# 53在PC端不能登录
zh = ["13527188051", "13527188046", "13527188053", "13527188054", "13527188055", "13527188042", "13527188056",
      "13527188041", "13527188057", "13527188058", "15814648648", "13527188071", "13527188072", "13527188073",
      "13527188074", "13527188075", "13527188076", "13527188077","13500123054","13500123051","13500123050","13500123053"]
q = 54


def login():
    driver.find_element_by_xpath(".//*[@id='password']").send_keys("123456")
    driver.find_element_by_xpath(".//*[@id='form']/div[5]/div[1]/div/label/input").click()
    driver.find_element_by_xpath(".//*[@id='form']/input[3]").click()
    sleep(1)
    driver.find_element_by_xpath(".//*[@id='goRecharge']").click()
    sleep(1)
    driver.find_element_by_xpath(".//*[@id='credit']").send_keys(q)
    h = driver.current_window_handle
    print h
    driver.find_element_by_xpath(".//*[@id='rechargeButton_quick']").click()
    driver.switch_to_window(driver.window_handles[1])
    sleep(1)
    # driver.find_element_by_xpath(".//*[@id='password']").send_keys("123456")
    # driver.find_element_by_xpath(".//*[@id='nextButton']").click()
    # driver.quit()

# index12 is 072
for i in range(5, 22):
    profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\e6bsauke.default'
    profile = webdriver.FirefoxProfile(profile_directory)
    driver = webdriver.Firefox(profile)
    driver.get("http://192.168.40.213:8086/")
    driver.maximize_window()
    driver.find_element_by_xpath("html/body/div[3]/div[2]/div[2]/section/p[3]/a").click()
    driver.find_element_by_xpath(".//*[@id='phone']").send_keys(zh[i])
    login()

