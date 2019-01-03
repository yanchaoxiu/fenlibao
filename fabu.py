# coding=utf-8
from pymouse import PyMouse
import SendKeys
from selenium.webdriver.support.select import Select
from time import sleep
from PIL import Image
import pytesseract
import math
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
driver=webdriver.Chrome()
url1 = 'http://192.168.40.236/pms/login'
driver.get(url1)
driver.maximize_window()  # 将浏览器最大化，以获取更清晰的校验码图片
ac1 = driver.current_url
print ac1
index="1"

def hqyzm():
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
    driver.find_element_by_xpath(".//*[@id='captcha']").send_keys(hqyzm())
    driver.find_element_by_xpath(".//*[@id='btn-submit']").click()
    sleep(1)


def xunhuan():
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
        xunhuan()


def fb():
    sleep(1)
    driver.find_element_by_xpath(".//*[@id='topmenu_container']/li[11]/a").click()
    sleep(1)
    driver.find_element_by_xpath("html/body/div[3]/div[2]/ul/li[3]/a").click()
    sleep(1)
    for i in range(1, 8):
        SendKeys.SendKeys("{RIGHT}")
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/table/tbody/tr[1]/td[14]/a").click()
    sleep(1)
    s12 = driver.find_element_by_xpath('//*[@id="lendType"]')
    Select(s12).select_by_index(index)
    sleep(1)
    driver.find_element_by_xpath("html/body/div[6]/div/div/div[3]/button[2]").click()
    # sleep(5)
    # driver.find_element_by_xpath("html/body/div[6]/div/div/div[2]/button").click()


hqyzm()
login()
xunhuan()
fb()
