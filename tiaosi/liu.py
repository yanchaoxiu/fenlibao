# coding=utf-8
from pymouse import PyMouse
import SendKeys
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from time import sleep
from PIL import Image
import pytesseract
import math
from selenium import webdriver

url = 'http://192.168.40.236/pms/login'
profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\e6bsauke.default'
profile = webdriver.FirefoxProfile(profile_directory)
driver = webdriver.Firefox(profile)
driver.maximize_window()  # 将浏览器最大化，以获取更清晰的校验码图片
driver.get(url)
ac1 = driver.current_url
print ac1


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
    sleep(3)


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

hqyzm()
login()
xunhuan()

sleep(3)
# driver.find_element_by_xpath(".//*[@id='topmenu_container']/li[11]/a").click()
# driver.find_element_by_xpath(".//*[@id='topmenu_container']/li[12]/a").click()
driver.find_element_by_link_text(u"业务管理").click()
sleep(2)
driver.find_element_by_xpath("html/body/div[3]/div[2]/ul/li[4]/a").click()
sleep(5)
def liu():
    driver.find_element_by_xpath(".//*[@id='loan_query']/button").click()
    sleep(2)
    driver.find_element_by_xpath(".//*[@id='loan-table']/tbody/tr[1]/td[14]/a[2]").click()
    sleep(1)
    driver.find_element_by_xpath("html/body/div[5]/div/div/div[3]/button[2]").click()
    sleep(2)
    driver.find_element_by_xpath("html/body/div[5]/div/div/div[2]/button").click()
    sleep(2)
    # driver.find_element_by_xpath(".//*[@id='loan_query']/button").click()
    # sleep(2)
for i in range(0,5):
    liu()
