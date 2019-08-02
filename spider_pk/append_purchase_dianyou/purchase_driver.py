#coding=utf-8
__author__ = 'shifeixiang'

from selenium import webdriver
import time

from pkten_log.pk_log import PkLog
pk_logger = PkLog('append_purchase_dianyou.purchase_driver').log()

def get_driver(username,password):
    #谷歌浏览器
    # chromedriver = "E:\\python\\webdriver\\chrome\\chromedriver37.exe"
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    # driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=options )

    #火狐浏览器
    driver = webdriver.Firefox(executable_path = 'E:\\python\\webdriver\\firefox\\geckodriver.exe')
    driver.get('http://pxkagme1.lot1068.net:8082/member/Welcome.action?searchKeyword=33588')

    driver.maximize_window();
    user_elem = driver.find_element_by_name("userCode")
    user_elem.send_keys(username)
    code_flag = True
    while(code_flag):
        try:
            pwd_elem = driver.find_element_by_name("password")
            pwd_elem.send_keys(password)
            #密码输入完毕后提供5s时间输入验证码
            time.sleep(10)
            #提交按钮

            js = "var q=document.documentElement.scrollTop=500"
            driver.execute_script(js)
            time.sleep(2)

            button = driver.find_element_by_xpath('//*[@id="loginForm"]/button')
            button.click()
            time.sleep(2)

            agree = driver.find_element_by_xpath('/html/body/div/div/a[1]')
            agree.click()
            time.sleep(2)
            code_flag = False
        except:
            pk_logger.info("please input code!")
            #print "please input code!"
            time.sleep(5)
            code_flag = True

    time.sleep(1)
    #跳转到top框架，获取北京10
    driver.switch_to_frame("topFrame")
    #print "top frameset1"
    time.sleep(1)

    #pk10
    pk10 = driver.find_element_by_xpath('//*[@id="201"]/a')
    pk10.click()
    time.sleep(1)

    # 1-10
    element_1_10 = driver.find_element_by_xpath('//*[@id="2011to10"]')
    element_1_10.click()
    time.sleep(1)
    #返回原始框架
    driver.switch_to_default_content()
    time.sleep(1)
    #切换到主框架
    driver.switch_to_frame("mainFrame")
    #print "switch mainFrame"
    time.sleep(1)
    #获取输入框
    #一般
    element_normal = driver.find_element_by_xpath('//*[@id="normalBetSlip"]')
    element_normal.click()
    time.sleep(3)
    print driver.current_url
    return driver

def reload_pk10_url(driver):
    #重新加载
    pk_logger.info("reload pk10,url:%s",driver.current_url)
    driver.get(driver.current_url)
    driver.switch_to_frame("topFrame")
    time.sleep(1)

    #pk10
    pk10 = driver.find_element_by_xpath('//*[@id="201"]/a')
    pk10.click()
    time.sleep(1)

    # 1-10
    element_1_10 = driver.find_element_by_xpath('//*[@id="2011to10"]')
    element_1_10.click()
    time.sleep(1)
    #返回原始框架
    driver.switch_to_default_content()
    time.sleep(1)
    #切换到主框架
    driver.switch_to_frame("mainFrame")
    time.sleep(1)
    #获取输入框
    #一般
    element_normal = driver.find_element_by_xpath('//*[@id="normalBetSlip"]')
    element_normal.click()
    time.sleep(1)
    #print driver.current_url
    return driver

