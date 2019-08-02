#coding=utf-8
__author__ = 'shifeixiang'
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver1():
    chromedriver = "E:\\python\\webdriver\\chrome\\chromedriver32.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=options )


    driver.get("http://pxiagme1.lot1068.net/member/Welcome.action?searchKeyword=99935")
    user_elem = driver.find_element_by_name("userCode")
    user_elem.send_keys("abab2233")
    code_flag = True
    while(code_flag):
        try:
            pwd_elem = driver.find_element_by_name("password")
            pwd_elem.send_keys("ABCd1234")
            # elem.send_keys(Keys.RETURN)
            time.sleep(5)

            button = driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/table/tbody/tr[5]/td[2]/input')
            button.click()
            time.sleep(5)

            agree = driver.find_element_by_xpath('/html/body/div/div/a[1]')
            agree.click()
            time.sleep(5)
            code_flag = False
        except:
            print "please input code!"
            code_flag = True
    # driver.get("http://pxiagme1.lot1068.net/member/pvn70lug1fsv2r3vng7cn049en/Home/Index.action")
    time.sleep(2)
    driver.switch_to_frame("topFrame")
    print "top frameset1"
    time.sleep(2)
    pk10 = driver.find_element_by_xpath('//*[@id="201"]/a')
    pk10.click()
    time.sleep(3)

    driver.switch_to_default_content()
    time.sleep(3)
    driver.switch_to_frame("mainFrame")
    print "switch mainFrame"
    time.sleep(3)
    input = driver.find_element_by_xpath('//*[@id="useDefaultStakeAmount"]')
    input.send_keys(100)
    time.sleep(5)

    driver.close()
    driver.quit()

def get_driver2():
    chromedriver = "E:\\python\\webdriver\\chrome\\chromedriver28.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=options )


    driver.get("http://pxiagme1.lot1068.net/member/p06c8m822otm4t4g970fkb7n7m/Home/Agree.action")
    # user_elem = driver.find_element_by_name("userCode")
    # user_elem.send_keys("abab2233")
    #
    # pwd_elem = driver.find_element_by_name("password")
    # pwd_elem.send_keys("ABCd1234")
    # elem.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.close()
    driver.quit()

def get_driver3():
    chromedriver = "E:\\python\\webdriver\\chrome\\chromedriver28.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=options )

    #driver.current_url
    # driver.get("http://pxiagme1.lot1068.net/member/Welcome.action?searchKeyword=99935")
    driver.get("http://pxiagme1.lot1068.net/member/fouvrh5q0rhl2edlk9m7jong3e/Welcome.action")
    #最大化
    # driver.maximize_window();
    user_elem = driver.find_element_by_name("userCode")
    user_elem.send_keys("abab2233")
    code_flag = True
    while(code_flag):
        try:
            pwd_elem = driver.find_element_by_name("password")
            pwd_elem.send_keys("ABCd1234")
            # elem.send_keys(Keys.RETURN)
            time.sleep(5)

            button = driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/table/tbody/tr[5]/td[2]/input')
            button.click()
            time.sleep(5)

            agree = driver.find_element_by_xpath('/html/body/div/div/a[1]')
            agree.click()
            time.sleep(5)
            code_flag = False
        except:
            print "please input code!"
            code_flag = True
    # driver.get("http://pxiagme1.lot1068.net/member/pvn70lug1fsv2r3vng7cn049en/Home/Index.action")
    time.sleep(2)
    #跳转到top框架，获取北京10
    driver.switch_to_frame("topFrame")
    print "top frameset1"
    time.sleep(2)

    pk10 = driver.find_element_by_xpath('//*[@id="201"]/a')
    pk10.click()
    time.sleep(3)

    # 1-10
    element_1_10 = driver.find_element_by_xpath('//*[@id="2011to10"]')
    element_1_10.click()
    time.sleep(3)
    #返回原始框架
    driver.switch_to_default_content()
    time.sleep(3)
    #切换到主框架
    driver.switch_to_frame("mainFrame")
    # driver.switch_to.frame()
    print "switch mainFrame"
    time.sleep(3)
    #获取输入框

    #一般
    element_normal = driver.find_element_by_xpath('//*[@id="normalBetSlip"]')
    element_normal.click()
    time.sleep(3)
    print driver.current_url
    continue_flag = True
    while(continue_flag):
        try:
            for i in range(3):
                xpath = '//*[@id="itmStakeInput20' + str(i+1) + '201"]'
                #第一名 big
                input_1_big = driver.find_element_by_xpath(xpath)
                input_1_big.send_keys(10-i)
                time.sleep(3)
             #确认按钮
            confirm = driver.find_element_by_xpath('//*[@id="memberMainContent"]/div[2]/table/tbody/tr/td[2]/a[1]')
            confirm.click()
            time.sleep(3)
            #提交按钮
            submit = driver.find_element_by_xpath('//*[@id="betSlipDivContent"]/table/tbody/tr[2]/td/a[1]')
                                                  # '//*[@id="betSlipDivContent"]/table/tbody/tr[3]/td/a[1]'
                                                  # '//*[@id="betSlipDivContent"]/table/tbody/tr[2]/td/a[1]'
            submit.click()
            time.sleep(3)
        except:
            print "封盘中...请稍后..."
            time.sleep(10)
            continue_flag = True

    #small '//*[@id="itmStakeInput201202"]'
    #单'//*[@id="itmStakeInput201301"]'
    #双'//*[@id="itmStakeInput201302"]'
    #1'//*[@id="itmStakeInput201101"]'
    #10'//*[@id="itmStakeInput201110"]'

    #第二名
    #大'//*[@id="itmStakeInput202201"]'
    #小'//*[@id="itmStakeInput202202"]'

    #单'//*[@id="itmStakeInput202301"]'
    #双'//*[@id="itmStakeInput202302"]'
    #1'//*[@id="itmStakeInput202101"]'
    #10'//*[@id="itmStakeInput202110"]'



    # input = driver.find_element_by_xpath('//*[@id="useDefaultStakeAmunt"]')
    # input.send_keys(100)
    time.sleep(5)

    driver.close()
    driver.quit()

def get_driver(username,password):
    chromedriver = "E:\\python\\webdriver\\chrome\\chromedriver28.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=options )


    driver.get("https://7989674523-bdgj.qq168.ws/login")
    # driver.get("http://pxiagme1.lot1068.net/member/fouvrh5q0rhl2edlk9m7jong3e/Welcome.action")
    driver.maximize_window();
    time.sleep(5)

    code_flag = True
    while(code_flag):
        try:
            user_elem = driver.find_element_by_name("account")
            # user_elem.send_keys("abab2233")
            user_elem.send_keys(username)

            pwd_elem = driver.find_element_by_name("password")
            # pwd_elem.send_keys("ABCd1234")
            pwd_elem.send_keys(password)
            # elem.send_keys(Keys.RETURN)
            #密码输入完毕后提供5s时间输入验证码
            time.sleep(5)
            #提交按钮
            button = driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[4]/input')
            button.click()
            time.sleep(2)

            agree = driver.find_element_by_xpath('/html/body/div/div/ul/li[2]/div/ul/li[15]/div/span/a[2]')
            agree.click()
            time.sleep(1)
            code_flag = False
        except:
            print "please input code!"
            time.sleep(5)
            code_flag = True
    # driver.get("http://pxiagme1.lot1068.net/member/pvn70lug1fsv2r3vng7cn049en/Home/Index.action")
    time.sleep(1)
    #跳转到top框架，获取北京10
    # driver.switch_to_frame("topFrame")
    # print "top frameset1"
    # time.sleep(1)

    #点击广告 '//*[@id="notClose2"]'
    ad = driver.find_element_by_xpath('//*[@id="notice_button1"]/a')
    ad.click()
    ad = driver.find_element_by_xpath('//*[@id="notice_button2"]/a')
    ad.click()
    #'//*[@id="notice_button1"]/a'
    # driver.find_element_by_xpath('//*[@id="notice_button1"]/a').click()

    print "---------"
    time.sleep(2)
    #pk10
    pk10 = driver.find_element_by_xpath('//*[@id="l_BJPK10"]/span')
    pk10.click()
    time.sleep(1)

    # 1-10
    element_1_10 = driver.find_element_by_xpath('//*[@id="sub_BJPK10"]/a[2]')
    element_1_10.click()
    time.sleep(1)

    print driver.current_url
    driver.switch_to_frame("frame")
    time.sleep(2)

    input_1_big = driver.find_element_by_xpath('1-2://*[@id="a_B1_2"]/input')
    input_1_big.send_keys(12)

    input_1_big = driver.find_element_by_xpath('1-2://*[@id="a_B1_3"]/input')
    input_1_big.send_keys(12)

    input_1_big = driver.find_element_by_xpath('1-2://*[@id="a_B1_2"]/input')
    input_1_big.send_keys(12)

    input_1_big = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/input[1]')
    input_1_big.click()
    time.sleep(1)

    input_1_big = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[1]/span')
    input_1_big.click()
    time.sleep(10)

    return driver


    continue_flag = True

    '1-1://*[@id="a_B1_1"]/input'
    '1-2://*[@id="a_B1_2"]/input'
    '2-1://*[@id="a_B2_1"]/input'
    '3-6://*[@id="a_B3_6"]/input'

    '确定://*[@id="header"]/div[2]/div/input[1]'

    '弹窗确定：/html/body/div[6]/div[3]/div/button[1]/span'


    while(continue_flag):
        try:
            for i in range(3):
                xpath = '//*[@id="itmStakeInput20' + str(i+1) + '201"]'
                #第一名 big
                input_1_big = driver.find_element_by_xpath(xpath)
                input_1_big.send_keys(10-i)
                time.sleep(3)
             #确认按钮
            confirm = driver.find_element_by_xpath('//*[@id="memberMainContent"]/div[2]/table/tbody/tr/td[2]/a[1]')
            confirm.click()
            time.sleep(3)
            #提交按钮
            submit = driver.find_element_by_xpath('//*[@id="betSlipDivContent"]/table/tbody/tr[2]/td/a[1]')
                                                  # '//*[@id="betSlipDivContent"]/table/tbody/tr[3]/td/a[1]'
                                                  # '//*[@id="betSlipDivContent"]/table/tbody/tr[2]/td/a[1]'
            submit.click()
            time.sleep(3)
        except:
            print "封盘中...请稍后..."
            time.sleep(10)
            continue_flag = True



def reload_pk10_url(driver):
    #重新加载
    print "reload pk10"
    driver.get(driver.current_url)
    driver.switch_to_frame("topFrame")
    print "top frameset1"
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
    # driver.switch_to.frame()
    print "switch mainFrame"
    time.sleep(1)
    #获取输入框
    #一般
    element_normal = driver.find_element_by_xpath('//*[@id="normalBetSlip"]')
    element_normal.click()
    time.sleep(3)
    print driver.current_url
    return driver


def get_xiazhu_message(purchase_number_str):
    buy_element_list = []
    purchase_number_str = '0,9|2|4|7,9|2|10|6,3|4|5|6|7|9,8|1|2|10,1|2|5|7|8|9,1|3|6|8|9|10'
    purchase_number_list = purchase_number_str.split(',')
    for index in range(len(purchase_number_list)):
        if purchase_number_list[index] == '0':
            pass
        else:
            purchase_numbers = purchase_number_list[index].split('|')
            for purchase_number in purchase_numbers:
                buy_element_list.append('//*[@id="a_B' + str(index+1) + '_' + str(purchase_number) + '"]/input')
    print buy_element_list


def get_xiazhu_message_trans(purchase_number_str):
    buy_element_list = []
    purchase_number_str = '0,9|2|4|7,9|2|10|6,3|4|5|6|7|9,8|1|2|10,1|2|5|7|8|9,1|3|6|8|9|10'
    base_set = set(['1','2','3','4','5','6','7','8','9','10'])
    # print base_set
    purchase_number_list = purchase_number_str.split(',')
    for index in range(len(purchase_number_list)):
        if purchase_number_list[index] == '0':
            pass
        else:
            purchase_numbers = purchase_number_list[index].split('|')
            purchase_numbers_set = set(purchase_numbers)
            # print "base",base_set
            # print "purchase",purchase_numbers_set
            trans_purchase_numbers =  list(base_set - purchase_numbers_set)
            for purchase_number in trans_purchase_numbers:
                buy_element_list.append('//*[@id="a_B' + str(index+1) + '_' + str(purchase_number) + '"]/input')
    print buy_element_list
    return buy_element_list


def test_scoller():
    chromedriver = "E:\\python\\webdriver\\chrome\\chromedriver36.exe"
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    # driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=options )
    driver = webdriver.Chrome(executable_path=chromedriver)


    driver.get("https://blog.csdn.net/u011541946/article/details/69681153")
    driver.maximize_window()

    js = "var q=document.documentElement.scrollTop=200"
    driver.execute_script(js)

    # print (driver.get_window_size())

    # driver.set_window_size(1280,800)
    # driver.get("http://pxiagme1.lot1068.net/member/fouvrh5q0rhl2edlk9m7jong3e/Welcome.action")
    # driver.maximize_window();
    time.sleep(5)

if __name__ == '__main__':
    # get_driver('yup98','aaa123')
    # get_xiazhu_message()
    # get_xiazhu_message_trans()
    test_scoller()