# coding:utf-8
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
xp=driver.find_element_by_xpath
driver.get("http://192.168.40.215:90/#/index")
# 登录
def login():
    xp("//*[@id='XSpop']/div/span/img").click()
    xp("//*[@id='app']/div[2]/section[2]/div[2]/a").click()
    xp("//*[@id='app']/div[2]/div[3]/section[2]/form/div[1]/input").send_keys("13527188071")
    xp("//*[@id='app']/div[2]/div[3]/section[2]/form/div[2]/input[1]").send_keys("123456")
    xp("//*[@id='app']/div[2]/div[3]/section[2]/form/div[4]/a").click()
    sleep(1)

# 出借
# driver.find_element_by_xpath("//*[@id='app']/div[2]/section[3]/ul/li/div[1]/div[1]/p").click()
# sleep(1)
# driver.find_element_by_xpath("//*[@id='app']/div[2]/section[3]/div/div[1]/a").click()
# driver.find_element_by_xpath("//*[@id='loanMoney']").send_keys("100")
# driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/a").click()
# driver.find_element_by_xpath("//*[@id='tipsCancel']").click()
# sleep(1)
# driver.find_element_by_xpath('//*[@id="pop-confirm"]/div/section/div[3]/div/a').click()

# 充值
login()
xp('//*[@id="app"]/div[2]/div[8]/nav/div/ul/li[4]/a/i').click()
sleep(1)
xp('//*[@id="app"]/div[2]/div[1]/section[2]/div[1]/a[2]/span').click()
sleep(1)
xp('//*[@id="app"]/div[2]/section[2]/input').send_keys("10")
xp('//*[@id="app"]/div[2]/section[3]/button').click()
sleep(2)
xp('//*[@id="password"]').send_keys("123456")
xp('//*[@id="nextButton"]').click()

# # 提现
# login()
# xp('//*[@id="app"]/div[2]/div[8]/nav/div/ul/li[4]/a/i').click()
# xp('//*[@id="app"]/div[2]/div[1]/section[2]/div[1]/a[1]/span').click()
# sleep(3)
# xp('//*[@id="app"]/div[2]/section[2]/div[1]/input').send_keys("12")
# xp('//*[@id="app"]/div[2]/div[3]/button').click()
# sleep(2)
# xp('//*[@id="password"]').send_keys("654321")
# xp('//*[@id="nextButton"]').click()

