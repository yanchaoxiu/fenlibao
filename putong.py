# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from PIL import Image
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import SendKeys
import pytesseract
driver=webdriver.Chrome()
driver.get("http://devdimeng.fenlibao.com/console/")
driver.maximize_window()
# 登录 MYFX YCFQ DEBX
biaoti=u"Dz0103_1"
type=u"DEBX"
month="2"
lilv="10"
money="1000000"
# 自动标index=0 手动标index=1
index="1"
xp=driver.find_element_by_xpath
def hqy():
    driver.save_screenshot('gps.png')  # 截取当前网页，该网页有我们需要的验证码
    imgelement = driver.find_element_by_xpath(".//*[@id='kaptcha']")  # 通过id定位验证码
    location = imgelement.location  # 获取验证码的x,y轴
    size = imgelement.size  # 获取验证码的长宽
    rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
    i = Image.open('gps.png')  # 打开截图
    verifycodeimage = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    verifycodeimage.save('verifycodeimage.png')
    image = Image.open('verifycodeimage.png')
    # print image
    vcode = pytesseract.image_to_string(image).strip()
    exclude_char_list = ' .:\\|\'\"?![],()~@#$%^&*_+-={};<>/¥'
    vcode = ''.join([x for x in vcode if x not in exclude_char_list])
    print (vcode)
    return (vcode)
def login():
    driver.find_element_by_xpath(".//*[@id='username']").send_keys("admin")
    driver.find_element_by_xpath(".//*[@id='password']").send_keys("123456")
    driver.find_element_by_xpath(".//*[@id='captcha']").send_keys(hqy())
    driver.find_element_by_xpath(".//*[@id='btn-submit']").click()
    sleep(1)
def xh():
    ac2 = driver.current_url
    while ac2 != ac1:
        print u"登录成功"
        break
    else:
        js1 = 'document.getElementById("tips").style.display="none";'
        driver.execute_script(js1)
        print u"登录失败"
        driver.refresh()
        login()
        xh()
def fb():
    sleep(1)
    driver.find_element_by_xpath(".//*[@id='topmenu_container']/li[11]/a").click()
    sleep(1)
    driver.find_element_by_xpath("html/body/div[3]/div[2]/ul/li[3]/a").click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="title"]').send_keys(biaoti)
    driver.find_element_by_xpath('//*[@id="searchBtn"]').click()
    sleep(1)
    for i in range(1, 8):
        SendKeys.SendKeys("{RIGHT}")
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/table/tbody/tr/td[14]/a").click()
    sleep(1)
    s12 = driver.find_element_by_xpath('//*[@id="lendType"]')
    Select(s12).select_by_index(index)
    sleep(1)
    driver.find_element_by_xpath("html/body/div[6]/div/div/div[3]/button[2]").click()
    # sleep(5)
    # driver.find_element_by_xpath("html/body/div[6]/div/div/div[2]/button").click()
def dm():
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
    xp(".//*[@id='userAccountLi']/input").send_keys("13794349509")
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
    xp(".//*[@id='nextStepButton']").click()
    sleep(2)
    xp(".//*[@id='saveBtn']/input[3]").click()
    sleep(3)
    s8 = xp(".//*[@id='entrustPayeeSelect']")
    Select(s8).select_by_value("0")
    xp(".//*[@id='form1']/div[1]/div[1]/ul/li[18]/div[2]/input").send_keys(u"技术")
    xp(".//*[@id='form1']/div[1]/div[1]/ul/li[19]/div[2]/input").send_keys(u"486号")
    s9 = xp(".//*[@id='subjectNatureSelect']")
    Select(s9).select_by_value("1")
    xp(".//*[@id='loanTitle']").send_keys(u"小姐姐")
    xp(".//*[@id='SB']/input[1]").click()
    xp(".//*[@id='SB']/input[2]").click()
    xp(".//*[@id='SB']/input[3]").click()
    xp(".//*[@id='test']").click()
    sleep(2)
    xp("html/body/div[5]/div/div[1]/div/div/div[2]/div[2]/div[2]/a[1]").click()

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
    driver.close()
dm()
driver=webdriver.Chrome()
driver.get('http://192.168.40.236/pms/login')
driver.maximize_window()
ac1 = driver.current_url
print ac1
hqy()
login()
xh()
fb()





