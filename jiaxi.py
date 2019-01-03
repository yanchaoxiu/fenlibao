# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\drmgdquc.default'
profile = webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox(profile)
driver.get("http://devdimeng.fenlibao.com/console/")
driver.maximize_window()
# 登录 MYFX YCFQ DEBX
biaoti=u"M债转1210_11"
type=u"MYFX"
month="2"
lilv="1"
money="2000"
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
sleep(2)
s1_1 = xp(".//*[@id='projectClassifyStr']")
Select(s1_1).select_by_value("BB")
xp(".//*[@id='contractCode']").send_keys("999")
xp(".//*[@id='userAccountLi']/input").send_keys("15088138955")
# # 旧版本的
# s1 = xp(".//*[@id='assetType']")
# Select(s1).select_by_value("3")

xp(".//*[@id='uploader']").send_keys(u"小姐姐")
xp(".//*[@id='loanTitle']").send_keys(biaoti)
s2 = xp(".//*[@id='tab1']/ul/li[8]/div[3]/select[1]")
Select(s2).select_by_value("440000")
s3 = xp(".//*[@id='tab1']/ul/li[8]/div[3]/select[2]")
Select(s3).select_by_value("440100")
s4 = xp(".//*[@id='xianSlt']")
Select(s4).select_by_value("440103")
xp(".//*[@id='address']").send_keys(u"486号")
xp(".//*[@id='jkje']").send_keys(money)
s5 = xp(".//*[@id='guaranteeMeasureSelect']")
Select(s5).select_by_value("3")
xp(".//*[@id='authTypeLi']/div[2]/input[1]").click()
xp(".//*[@id='authTypeLi']/div[2]/input[2]").click()
xp(".//*[@id='authTypeLi']/div[2]/input[3]").click()
s6 = xp(".//*[@id='jkytSelect']")
Select(s6).select_by_value(u"资金周转")
xp(".//*[@id='jkqx']").clear()
xp(".//*[@id='jkqx']").send_keys(month)
xp(".//*[@id='annualRate']").send_keys(lilv)
xp(".//*[@id='borrowerInterestRate']").send_keys("30")
s10 = xp(".//*[@id='hkfs']")
Select(s10).select_by_value(type)
s7 = xp(".//*[@id='hklySelect']")
Select(s7).select_by_value(u"工资收入")

# 营销设置
driver.find_element_by_xpath(".//*[@id='checkMarketingSetting']").click()
driver.find_element_by_xpath(".//*[@id='rateInterestForBid']").clear()
driver.find_element_by_xpath(".//*[@id='rateInterestForBid']").send_keys("5")
driver.find_element_by_xpath(".//*[@id='checkTotalUserAssets']").click()
driver.find_element_by_xpath(".//*[@id='totalUserAssets']").send_keys("200")


driver.find_element_by_xpath(".//*[@id='nextStepButton']").click()
sleep(2)
driver.find_element_by_xpath(".//*[@id='saveBtn']/input[3]").click()
sleep(2)
s8 = driver.find_element_by_xpath(".//*[@id='entrustPayeeSelect']")
Select(s8).select_by_value("0")
driver.find_element_by_xpath(".//*[@id='form1']/div[1]/div[1]/ul/li[18]/div[2]/input").send_keys(u"技术")
driver.find_element_by_xpath(".//*[@id='form1']/div[1]/div[1]/ul/li[19]/div[2]/input").send_keys(u"489号")
s9 = driver.find_element_by_xpath(".//*[@id='subjectNatureSelect']")
Select(s9).select_by_value("1")
driver.find_element_by_xpath(".//*[@id='loanTitle']").send_keys(u"小姐姐")
driver.find_element_by_xpath(".//*[@id='SB']/input[1]").click()
driver.find_element_by_xpath(".//*[@id='SB']/input[2]").click()
driver.find_element_by_xpath(".//*[@id='SB']/input[3]").click()
driver.find_element_by_xpath(".//*[@id='test']").click()
sleep(2)
driver.find_element_by_xpath("html/body/div[5]/div/div[1]/div/div/div[2]/div[2]/div[2]/a[1]").click()
# 审核
sleep(1)
xp(".//*[@id='form_loan']/div/div[1]/div[2]/div[1]/p[2]/input").send_keys(biaoti)
xp(".//*[@id='form_loan']/div/div[1]/div[2]/div[1]/div[2]/input").click()
sleep(1)
xp(".//*[@id='form_loan']/div/div[2]/table/tbody/tr[2]/td[15]/a[1]").click()
sleep(1)
xp("html/body/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/div/ul/li[4]/a").click()
sleep(1)
xp("html/body/div[5]/div/div[1]/div/div/div[2]/div[2]/div[2]/a[1]").click()
sleep(1)
xp("html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]").click()