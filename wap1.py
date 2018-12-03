# coding:utf-8
from selenium import webdriver
from time import sleep
import SendKeys
zh = ["13527188051", "13527188046", "13527188053", "13527188054", "13527188055", "13527188042", "13527188056",
      "13527188041", "13527188057", "13527188058", "15814648648", "13527188071", "13527188072", "13527188073",
      "13527188074", "13527188075", "13527188076", "13527188077","13500123054","13500123051","13500123050","13500123053"]
q = 100
def login():
    driver.find_element_by_xpath("/html/body/div[2]/div[3]/section[2]/form/div[2]/input[1]").send_keys("123456")
    driver.find_element_by_xpath("/html/body/div[2]/div[3]/section[2]/form/div[4]/button").click()
    driver.find_element_by_xpath("/html/body/nav/div/ul/li[4]/a/p").click()
    driver.find_element_by_xpath("/html/body/div[2]/section[2]/div[1]/a[2]/span").click()
    driver.find_element_by_xpath("/html/body/div[2]/section[2]/input").send_keys(q)
    h = driver.current_window_handle
    print h
    driver.find_element_by_xpath("/html/body/div[2]/section[3]/button").click()
    # driver.switch_to_window(driver.window_handles[1])
    driver.find_element_by_xpath(".//*[@id='password']").send_keys("123456")
    driver.find_element_by_xpath(".//*[@id='nextButton']").click()
    driver.quit()
# index12 is 072
for i in range(0, 1):
    driver = webdriver.Chrome()
    driver.get("http://192.168.40.238:81/?#lotteryIn")
    # driver.maximize_window()
    # SendKeys.SendKeys("{F12}")
    # sleep(1)
    driver.find_element_by_xpath("//*[@id='XSpop']/div/span").click()
    driver.find_element_by_xpath("/html/body/div[3]/section[2]/div[2]/a").click()
    driver.find_element_by_xpath("/html/body/div[2]/div[3]/section[2]/form/div[1]/input").send_keys(zh[i])
    login()